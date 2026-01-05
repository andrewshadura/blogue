---
layout: post
title: "Rust-like enums in Kotlin"
date: 2019-09-25T15:31:43
lastmod: 2019-09-25T15:31:43
comments: true
tags: ["Android", "Kotlin", "Rust"]
slug: kotlin-enums
---

Rust has an exciting concept of enumeration types, which is much more powerful than enums in other languages.
Notably C has the weakest type of enum, since there’s no type checking of any kind, and enum values can be used interchangeably with integers:

    :::c
    enum JobState {
        PENDING,
        STARTED,
        FAILED,
        COMPLETED
    };

You can opt for manually assigning integers instead of leaving this to the compiler, but that’s about it.

Higher level languages like Python and Java treat enumeration types as classes, bringing stricted type checking and better flexibility, since they can be extended nearly as any other classes. In both Python and Java individual enumerated values are singleton instances of the enumeration class.

    :::python
    class JobState(Enum):
        PENDING = auto()
        STARTED = auto()
        FAILED = auto()
        COMPLETED = auto()

```
:::java
enum JobState {
    PENDING,
    STARTED,
    FAILED,
    COMPLETED;
}
```
Since enumerations are classes, they can define extra methods, but because the enum values are singletons, they can’t be coupled with any extra data, and no new instances of the enum class can be created.

In contrast with Python and Java, Rust allows attaching data to enumerations:

    :::rust
    enum JobState {
        Pending,
        Started,
        Failed(String),
        Completed
    }

This allows us to store the error message in the same value as the job state, without having to declare a structure with an extra field which would be used only when the state in `Failed`.

So, what Kotlin has to offer? Kotlin has a language feature called *sealed classes*. A sealed class is an abstract class with limited interitance: all of its subclasses have to be declated in the same file. In a way, this is quite close to the Rust enums, even though sealed classed look and behave a bit differently.

    :::kotlin
    sealed class JobState {
        object Pending : JobState()
        object Started : JobState()
        object Completed : JobState()
        data class Failed(val errorMessage: String) : JobState()
    }

Declared this way, `JobState` can be used in a way similar to Rust’s enums: a single variable of this type can be assigned singletons `Pending`, `Started` or `Completed`, or any instance of `Failed` with a mandatory `String` member:

    :::kotlin
    val state: JobState = JobState.Failed("I/O error")

    when (state) {
        is JobState.Completed ->
            println("Job completed")
        is JobState.Failed ->
            println("Job failed with an error: ${state.errorMessage}")
    }

This usage resembles the regular Java/Kotlin enums quite a bit, but alternatively, `Pending` and friends can be declared outside of the sealed class, allowing them to be used directly without the need to add a `JobState` qualifier.

A slightly simplified real life example from a Kotlin project I’m working on, where a separate coroutine handles I/O with a Bluetooth or a USB device:

```
:::kotlin
sealed class Result
object Connected : Result()
data class Failed(val error: String) : Result()

sealed class CommServiceMsg
data class Connect(val response: CompletableDeferred<Result>) : CommServiceMsg()
object Disconnect : CommServiceMsg()
data class Write(val data: ByteArray) : CommServiceMsg()

fun CoroutineScope.bluetoothServiceActor(device: BluetoothDevice) = actor<CommServiceMsg>(Dispatchers.IO) {
    val socket: BluetoothSocket = device.createSocket()

    process@ for (msg in channel) {
        when (msg) {
            is Connect -> {
                with(socket) {
                    msg.response.complete(try {
                        connect()
                        Connected
                    } catch (e: IOException) {
                        val error = e.message ?: ""
                        Failed(error)
                    }
                }
            }
            is Disconnect -> break@process
            is Write -> {
                socket.outputStream.write(msg.data)
            }
        }
    }
    socket.outputStream.flush()
    socket.close()
}
```

Here, we can talk to `bluetoothServiceActor` using messages each carrying extra data; if the coroutine needs to talk back (in this example, the result of a connection attempt), it uses a `CompletableDeferred<>` value of the `Result` type, which can hold an error message when needed.

With that in place, we can write something like this:

```
:::kotlin
val bluetoothService = bluetoothServiceActor(device)
val response = CompletableDeferred<Result>()

bluetoothService.send(Connect(response))
var result = response.await()
when (result) {
    is Connected -> {
        bluetoothService.send(Write(byteArrayOf(42, 0x1e, 0x17)))
        bluetoothService.send(Disconnect)
    }
    is Failed ->
        println("error occurred: ${result.error}")
}
```

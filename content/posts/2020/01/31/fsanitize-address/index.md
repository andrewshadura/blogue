---
layout: post
title: Using gcc sanitisers to get a nasty bug fixed
date: 2020-01-31T12:35:45
lastmod: 2020-01-31T12:35:45
comments: true
tags: ["valgrind", "address sanitiser", "gcc", "linter", "Apertis", "Debian"]
slug: fsanitize-address
---

A couple of days ago a colleague at [Collabora](https://www.collabora.com/) asked me to help create a Debian package for the tool he needed to complete his task. The tool happened to be an NXP code signing tool, used to sign OS images to be run on i.MX systems using ‘*High Assurance Boot*’.

As it often happens, the tool was distributed in a manner typical for many big corporations: no direct link to the tarball, custom buildsystem, compiled binaries in the same tarball as the sources. A big relief was that the tool has been distributed under a three-clause BSD license since version 3.3.0 (the sources were not provided at all before that).

The custom buildsystem meant it was not using the Debian build flags (`CFLAGS := …`, `CC := gcc`), so I had to plug a custom ‘toolchain’ Makefile into the right place with definitions relevant to Debian:

```makefile
DPKG_EXPORT_BUILDTOOLS = 1

include /usr/share/dpkg/buildtools.mk

LD = $(CC)

COPTIONS += -std=c99 -D_POSIX_C_SOURCE=200809L -fPIC $(shell dpkg-buildflags --get CPPFLAGS) $(shell dpkg-buildflags --get CFLAGS)

LDOPTIONS += $(shell dpkg-buildflags --get LDFLAGS)
```

After some time of playing with the build system, the package was done and sent to a colleague pending an upload to Debian. What did worry me a bit was a weird warning the compiler gave me every time:

```shell
../../code/front_end/src/acst.c: In function ‘encrypt_images’:
../../code/front_end/src/acst.c:791:25: warning: argument 1 value ‘18446744073709551615’ exceeds maximum object size 9223372036854775807 [-Walloc-size-larger-than=]
  791 |         uint8_t *hash = malloc(hash_size);
      |                         ^~~~~~~~~~~~~~~~~
```

We didn’t use encryption, so I didn’t feel motivated to investigate.

Bad move.

Next day, the colleague comes back to me with this:

> I did test builds in Apertis SDK, Debian buster, Fedora 31, ALT Linux 9 -- only the latter environment produced the `cst` tool which generated correct signature for the file.
> 
> The rest produce a bit different signature with zeroes for the current kernel:
> 
>     000007E9 00 30
>     000007EA 00 82
>     000007EB 00 01
>     000007EC 00 F9
>     00000D41 00 30
>     00000D42 00 82
>     00000D43 00 01
>     00000D44 00 F9
> 
> I found that the problem is related to compilation of `code/front_end/src/cst.c`.

The colleague sent me a tarball with the working binary and a simple test case.

### First attempt

Okay, let’s see. What are those eight different bytes? The signing tool comes with a utility, `csf_parser` to look inside of the signed file and extract bits and pieces. With debug logs on, for the correctly signed file the logs say this:

```
CSF TAG: 0xD8
Parsing following values
0xD8 0x02 0x01 0x40 0x30 0x82 0x01 0xF9 0x06 …
```

The incorrectly signed one has this:

```
CSF TAG: 0xD8
Parsing following values
0xD8 0x02 0x01 0x40 0x00 0x00 0x00 0x00 0x06 …
```

What’s 0xD8? `hab_types.h` says:

```c
#define HAB_TAG_SIG  0xd8         /**< Signature */
```

Apparently, the first four bytes are a header of the data chunk, so the differing bytes are part of the signature itself.

Let’s add some debug prints to see what’s going on. Oh no: now the difference is not just 8 bytes, but much more. Looks like there’s some memory corruption or undefined behaviour or maybe both.

Meanwhile, the colleague chimes in: he tried linking `cst.o` from ALT Linux with the rest of the program built on Debian, and produced a working binary.

### The dead end: disassembly

My first thought was: oh, it’s just some code relying on undefined behaviour, what if I decompiled both object files and compared them?

In the past, when I needed to disassemble something I used IDA, but since it’s proprietary, I never had a license for it, and I don’t have it anymore anyway, it was not an option. It did, however, have a very good decompilation module which produced mostly readable C-like pseudocode.

When a couple of years ago I looked for a free software replacement for IDA, radare seemed like it had some potential, but it didn’t seem ready, and it wasn’t fully packaged for Debian. The things have changed, and not only radare is in Debian, but it also comes with a GUI, Cutter, which is very good, even though there’s always toom for improvement.

To my surprise, it turned out radare also has some decompilation functionality which worked really well.

Anyway, I won’t go further into it since this experiment didn’t give me any useful data to work with.

### Trying it with gdb

Good, so the code at fault is somewhere close to the signing functions, so let’s try and debug it.

I rarely use the command-line gdb for anything else than printing backtraces, so here’s a small cheatsheet for the next time I need it:

* `break -func create_sig_file`: set breakpoint at a function
* `finish`: ‘step out’, run to the end of the current function and stop right after it returns
* `x/10xb pointer`: print **10** he**x**adecimal **b**ytes

This is what I have figured during my debugging session: the data gets corrupted at the end of the signing sequence, inside or before the `cms_to_buf` function invocation, which gets the signature data copied from the internal OpenSSL data structure into the output buffer:

    (gdb) finish
    Run till exit from #0  cms_to_buf (cms=cms@entry=0x555555598a60, bio_in=bio_in@entry=0x555555597ff0, 
        data_buffer=data_buffer@entry=0x7fffffffd380 "\003", data_buffer_size=data_buffer_size@entry=0x7fffffffd37c, 
        flags=flags@entry=17090) at ../../code/back_end/src/adapt_layer_openssl.c:364
    0x0000555555564399 in gen_sig_data_cms (sig_buf_bytes=0x7fffffffd37c, sig_buf=0x7fffffffd380 "", 
        hash_alg=<optimised out>, key_file=0x555555578f70 "IMG1_1_sha256_2048_65537_v3_usr_key.pem", 
        cert_file=0x555555591440 "IMG1_1_sha256_2048_65537_v3_usr_crt.pem", in_file=<optimised out>)
        at ../../code/back_end/src/adapt_layer_openssl.c:487
    487    in ../../code/back_end/src/adapt_layer_openssl.c
    Value returned is $2 = 0
    (gdb) x/10xb 0x7fffffffd380
    0x7fffffffd380:    0x00    0x00    0x00    0x00    0x06    0x09    0x2a    0x86
    0x7fffffffd388:    0x48    0x86

    (gdb) finish
    Run till exit from #0  cms_to_buf (cms=0x445290, bio_in=0x444800, 
        data_buffer=0x7fffffffcbe0 "P\320\377\377\377\177", data_buffer_size=0x7fffffffcbcc, flags=17090)
        at ../../code/back_end/src/adapt_layer_openssl.c:365
    0x00000000004109f6 in gen_sig_data_cms (in_file=0x416553 "imgsig.bin", 
        cert_file=0x43dc50 "IMG1_1_sha256_2048_65537_v3_usr_crt.pem", 
        key_file=0x43d640 "IMG1_1_sha256_2048_65537_v3_usr_key.pem", hash_alg=SHA_256, 
        sig_buf=0x7fffffffcbe0 "0\202\001\371\006\t*"..., 
        sig_buf_bytes=0x7fffffffcbcc) at ../../code/back_end/src/adapt_layer_openssl.c:487
    487    in ../../code/back_end/src/adapt_layer_openssl.c
    Value returned is $5 = 0
    (gdb) x/10xb 0x7fffffffcbe0
    0x7fffffffcbe0:    0x30    0x82    0x01    0xf9    0x06    0x09    0x2a    0x86
    0x7fffffffcbe8:    0x48    0x86

### Trying it with splint and valgrind

Having failed to find the data corruption by manually inspecting the source, I tried enabling every compiler warning I could, which gave me no results, and then decided to use external tools to help me with that.

First comes *splint*, a C linter. It produced about a thousand warnings and errors which, while probably were at least partially valid, completely overwhelmed me.

Next came *valgrind*, which, even at the most aggressive settings only pointed me at uninitialised padding data in some structures:

```yacc
number:  NUMBER
        {
            $$ = malloc(sizeof(number_t));
            $$->next = NULL;
            $$->num_value = $1;
        }
        ;
```

And, of course, OpenSSL was reading uninitialised data to improve the randomness.

Not very helpful.

### Almost giving up

Since I have spent most of the day debugging, valgrinding, reading code and worrying about my soon to be missed [connection to Brussels in Frankfurt](/2020/01/28/fosdem-by-train/), I became very frustrated about having no useful results and was close to giving up and calling it a day.

As a last chance attempt, I decided to try all hardening options I could find in the GCC manual page and on the Debian wiki.

First, `DEB_BUILD_MAINT_OPTIONS = hardening=+all`, `-fPIE -pie`. Not much changed. Or rather nothing at all.

Then, I found sanitisers. Okay, dump it all into the makefile: `-fsanitize=address -fsanitize=undefined -fsanitize=leak -fno-omit-frame-pointer`. Compile, link, run: nothing works. Apparently, they need link options as well: `-static-libasan -static-libubsan -static-liblsan`

{{< figure "img-responsive" "asan.png" "Colourful address sanitiser output" "" >}}

Cracked it!

```c
/**
 * sig_size as input to gen_sig_data shows the size of buffer for
 * signature data and gen_sig_data returns actual size of signature
 * data in this argument
 */
uint32_t sig_size = SIGNATURE_BUFFER_SIZE;

...

/**
 * Calling gen_sig_data to generate signature for data in file using
 * certificate in cert_file. The signature data will be returned in
 * sig and size of signature data in sig_size
 */
ret_val = gen_sig_data(file, cert_file, hash, sig_fmt,
    sig, (size_t *)&sig_size, g_mode);
```

Of course, `size_t` is 32-bit on 32-bit systems, but *significantly* wider on 64-bit ones, so no surprise this code would overwrite something else on the stack, in this case the signature data.

One of the lessons I learnt from this way: never underestimate the compiler’s built-in tools. At least, not the sanitisers!

Oh, just in case you want to see more: the patches currently live at the [Apertis GitLab](https://gitlab.apertis.org/pkg/development/imx-code-signing-tool/merge_requests/2/).

**2020-02-18 Update**: This post has also been published at Collabora’s website: <https://www.collabora.com/news-and-blog/blog/2020/02/18/using-gcc-sanitisers-to-get-a-nasty-bug-fixed>

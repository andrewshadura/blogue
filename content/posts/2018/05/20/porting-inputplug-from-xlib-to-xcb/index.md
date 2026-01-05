---
title: Porting inputplug to XCB
date: 2018-05-20T21:50:00
lastmod: 2018-05-20T21:50:00
slug: porting-inputplug-from-xlib-to-xcb
comments: true
---

5 years ago I wrote [inputplug](https://bitbucket.org/andrew_shadura/inputplug), a tiny
daemon which connects to your X server and monitors its input devices, running an external
command each time a device is connected or disconnected.

I have used a custom keyboard layout and a fairly non-standard settings for my pointing
devices since 2012. I always annoyed me those settings would be re-set every time the device
was disconnected and reconnected again, for example, when the laptop was brought back up from
the suspend mode. I usually solved that by putting commands to reconfigure my input settings
into the resume hook scripts, but that obviously didn’t solve the case of connecting external
keyboards and mice. At some point those hook scripts stopped to work because they would run too
early when the keyboard and mice were not they yet, so I decided to write inputplug.

Inputplug was the first program I ever wrote which used X at a low level, and I had to use
Xlib to access the low-level features I needed. More specifically, inputplug uses XInput
X extension and listens to `XIHierarchyChanged` events. In June 2014, Vincent Bernat
[contributed](https://bitbucket.org/andrew_shadura/inputplug/commits/87bea9b7f8766c109b1ec89b78778677fc70ab23)
a patch to rely on XInput2 only.

During the [MiniDebCamp](https://wiki.debian.org/DebianEvents/de/2018/MiniDebConfHamburg), I had a
typical case of yak shaving despite not having any yaks around: I wanted to migrate inputplug’s
packaging from Alioth to Salsa, and I had an idea to update the package itself as well. I had
an idea of adding optional systemd user session integration, and the easiest way to do that
would be to have inputplug register a D-Bus service. However, if I just registered the service,
introspecting it would cause annoying delays since it wouldn’t respond to any of the messages
the clients would send to it. Handling messages would require me to integrate polling into the
event loop, and it turned out it’s not easy to do while sticking to Xlib, so I decided to try
and port inputplug to XCB.

For those unfamiliar with XCB, here’s a bit of background: XCB is a library which implements
the X11 protocol and operates on a slightly lower level than Xlib. Unlike Xlib, it only works
with structures which map directly to the wire protocol. The functions XCB provides are really
atomic: in Xlib, it not unusual for a function to perform multiple X transactions or to juggle
the elements of the structures a bit. In XCB, most of the functions are relatively thin wrappers
to enable packing and unpacking of the data. Let me give you an example.

In Xlib, if you wanted to check whether the X server supports a specific extension, you would write
something like this:

```
:::c
XQueryExtension(display, "XInputExtension", &xi_opcode, &event, &error)
```

Internally, `XQueryExtension` would send a QueryExtension request to the X server, wait
for a reply, parse the reply and return the major opcode, the first event code and the
first error code.

With XCB, you need to separately send the request, receive the reply and fetch the data you need
from the structure you get:

```
:::c
const char ext[] = "XInputExtension";

xcb_query_extension_cookie_t qe_cookie;
qe_cookie = xcb_query_extension(conn, strlen(ext), ext);

xcb_query_extension_reply_t *rep;
rep = xcb_query_extension_reply(conn, qe_cookie, NULL);
```

At this point, `rep` has its field `preset` set to `true` if the extension is present. The rest
of the things are in the structure as well, which you have to `free` yourself after the use.

Things get a bit more tricky with requests returning arrays, like `XIQueryDevice`. Since the
`xcb_input_xi_query_device_reply_t` structure is difficult to parse manually, XCB provides an
iterator, `xcb_input_xi_device_info_iterator_t` which you can use to iterate over the structure:
`xcb_input_xi_device_info_next` does the necessary parsing and moves the pointer so that each
time it is run the iterator points to the next element.

Since replies in the X protocol can have variable-length elements, e.g. device names, XCB also
provides wrappers to make accessing them easier, like `xcb_input_xi_device_info_name`.

Most of the code of XCB is generated: there is an XML description of the X protocol which is used
in the build process, and the C code to parse and generate the X protocol packets is generated each
time the library is built. This means, unfortunately, that the [documentation](https://xcb.freedesktop.org/manual/)
is quite useless, and there aren’t many examples online, especially if you’re going to use rarely
used functions like XInput hierarchy change events.

I decided to do the porting the hard way, changing Xlib calls to XCB calls one by one, but there’s an
[easier way](https://xcb.freedesktop.org/MixingCalls/): since Xlib is now actually *based on XCB*, you can `#include <X11/Xlib-xcb.h>` and use
`XGetXCBConnection` to get an XCB connection object corresponding to the Xlib’s `Display` object.
Doing that means there will still be a single X connection, and you will be able to mix Xlib and
XCB calls.

When porting, it often is useful to have a look at the sources of Xlib: it becomes obvious what XCB functions
to use when you know what Xlib does internally (thanks to Mike Gabriel for pointing this out!).

Another thing to remember is that the constants and enums Xlib and XCB define usually have the same values
(mandated by the X protocol) despite having slightly different names, so you can mix them too. For example,
since inputplug passes the XInput event names to the command it runs, I decided to keep the names as Xlib
defines them, and since I’m creating the corresponding strings by using a C preprocessor macro, it was easier
for me to keep using `XInput2.h` instead of defining those strings by hand.

If you’re interested in the result of this porting effort, have a look at [the code in the Mercurial repo](https://bitbucket.org/andrew_shadura/inputplug/commits/d51dad6b9736813fe9e0612b38db43b623c9a335). Unfortunately, it cannot be packaged for Debian yet since the
Debian package for XCB doesn’t ship the module for XInput (see bug #[733227](https://bugs.debian.org/733227)).

P.S. Thanks again to Mike Gabriel for providing me important help — and explaining where to look for more of it ;)


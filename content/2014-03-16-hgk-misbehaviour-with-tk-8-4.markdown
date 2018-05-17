---
layout: post
title: "hgk misbehaviour with Tk 8.4"
date: 2014-03-16 11:31
comments: true
slug: hgk-misbehaviour-with-tk-8-4
tags: 
---

Strangely enough, running hgk (a port of gitk to Mercurial, also known as `hg view`) with Tk 8.4 crashes my X server. Updating both Tk and the X doesn't help. I don't feel like I want to debug X now, but probably that's what I have to do :(
<pre>
Backtrace:
0: /usr/bin/X (xorg_backtrace+0x49) [0xb7712ed9]
1: /usr/bin/X (0xb7572000+0x1a4c64) [0xb7716c64]
2: linux-gate.so.1 (__kernel_rt_sigreturn+0x0) [0xb755040c]
3: /lib/i386-linux-gnu/i686/cmov/libc.so.6 (0xb711d000+0x772f0) [0xb71942f0]
4: /lib/i386-linux-gnu/i686/cmov/libc.so.6 (__libc_calloc+0xab) [0xb7196d5b]
5: /usr/bin/X (0xb7572000+0x55ca9) [0xb75c7ca9]
6: /usr/bin/X (0xb7572000+0x48005) [0xb75ba005]
7: /usr/bin/X (0xb7572000+0x491c3) [0xb75bb1c3]
8: /usr/bin/X (0xb7572000+0x12c621) [0xb769e621]
9: /usr/bin/X (XkbHandleActions+0x20b) [0xb76c8c1b]
10: /usr/bin/X (XkbProcessKeyboardEvent+0xbc) [0xb76c937c]
11: /usr/bin/X (AccessXFilterPressEvent+0xcd) [0xb76c181d]
12: /usr/bin/X (0xb7572000+0x157675) [0xb76c9675]
13: /usr/bin/X (mieqProcessDeviceEvent+0x1e6) [0xb76f3226]
14: /usr/bin/X (mieqProcessInputEvents+0xfd) [0xb76f335d]
15: /usr/bin/X (ProcessInputEvents+0x14) [0xb75ef3e4]
16: /usr/bin/X (0xb7572000+0x3c25d) [0xb75ae25d]
17: /usr/bin/X (0xb7572000+0x2a51a) [0xb759c51a]
18: /lib/i386-linux-gnu/i686/cmov/libc.so.6 (__libc_start_main+0xf5) [0xb71368c5]
19: /usr/bin/X (0xb7572000+0x2a8f8) [0xb759c8f8]
</pre>

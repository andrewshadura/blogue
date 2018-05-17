---
layout: post
title: "Tired of autotools? Try this: mk-configure"
date: 2014-03-24 23:30
comments: true
slug: mk-configure-tired-of-autotools-try-this
tags: 
---

[mk-configure](http://sourceforge.net/projects/mk-configure/) is a project which tries to be autotools done right.
Instead of supporting an exceedingly large number of platforms, modern and ancient, at costs of generated unreadable
multi-kilobyte shell scripts, mk-configure aims at better support of less platforms, but those which are really in
use today. One of the main differences of this project is that it avoids code generation as much as possible.
The author of mk-configure, Aleksey Cheusov, a 38 years old NetBSD hacker from Belarus, uses NetBSD make (*bmake*)
and shell script snippets instead of monstrous libraries written in *m4* interleaved with shell scripts. As the result,
there's no need in a separate step of package configuration or bootstrapping the configure script, everything is done
by just running `bmake`, or a convenience wrapper for it, `mkcmake`, which prepends a proper library path to bmake
arguments, so you don't have to specify it yourself.

Today, mk-configure is already powerful enough to be able replace autotools for most of the projects, and what is missing
from it can be easily done by hacking the Makefile, which would otherwise be quite simple.

Try it for your project, you may really like it. I already did. And [report bugs](http://github.com/cheusov/mk-configure/issues).

---
layout: post
title: "Process isolation support in start-stop-daemon"
date: 2014-03-08T11:17:00
lastmod: 2014-03-08T11:17:00
comments: true
tags: []
---

Yesterday I played with LXC a bit, and I liked it, as LXC provides a
very lightweight isolation of processes, much like enchanced chroot.
However, I realised, I don't always need the chroot-like part of LXC,
sometimes what I need is just to make sure the process is unable to
see the other processes and talk to them in any other way except the
filesystem, but I don't want a whole separate root file system for
that. LXC provides a simple utility, `lxc-unshare`, which uses
Linux-specific clone(2) call to run a process with new PID, IPC and other
namespaces. However, this utility can't be used for running forking
daemons, as the container is destroyed when its PID 1 exits.

That's why I decided to add the support for process isolation to `start-stop-daemon`.
I was careful enough to introduce minimal changes to it to make sure they can
be merged back to the version as shipped with `dpkg`, and at the same time
be buildable separately from the rest of it. Speaking of building, by the way,
this version of `start-stop-daemon` uses [mk-configure](http://sourceforge.net/projects/mk-configure/),
a light-weight autotools replacement, as its build system.

What I added, from a user's perspective, is a single `--isolate` option. When
run with this option, `start-stop-daemon` calls clone(2) just before configuring
the environment of a process it's going to run. The cloned process runs in
a new namespace, and immediately remounts `/proc`, `/dev/shm` and `/dev/mqueue`.
Then it forks, and a forked process executes the daemon. The parent process,
which is PID 1 in the new PID namespace, uses waitpid(2) to monitor its child
processes. As soon as its very first child exits, it talks via a pipe to the process
outside of the container, so that it knows the container has a forked daemon
and it needs to detach. In any case, the container's PID 1 does waitpid(2) in
a loop, checking the process list every time a child terminates. As soon as it's left
alone or a `SIGTERM` is received, it exits.

The code is published at [Bitbucket](https://bitbucket.org/andrew_shadoura/start-stop-daemon-isolate).

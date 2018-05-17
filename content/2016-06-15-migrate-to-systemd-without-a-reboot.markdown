---
layout: post
title: "Migrate to systemd without a reboot"
date: 2016-06-15 13:51
comments: true
tags: systemd
---

Yesterday I was fixing [an issue](https://bitbucket.org/conservancy/kallithea/pull-requests/235/minor-changes/diff#comment-19707125) with one of the servers behind [kallithea-scm.org](https://kallithea-scm.org): the hook intended to propagage pushes from Our Own Kallithea to Bitbucket stopped working. Until yesterday, that server was using Debian’s flavour of System V init and djb’s dæmontools to keep things running. To make the hook asynchronous, I wrote a service to be managed to dæmontools, so that concurrency issued would be solved by it. However, I didn't implement any timeouts, so when last week `wget` froze while pulling Weblate's hook, there was nothing to interrupt it, so the hook stopped working since dæmontools thought it's already running and wouldn’t re-trigger it. Killing `wget` helped, but I decided I need to do something with it to prevent the situation from happening in the future.

I’ve been using systemd at [work](https://collabora.co.uk/) for the last year, so I am now confident I'm happier with systemd than with dæmontools, so I decided to switch the server to systemd. Not surprisingly, I prepared unit files in about 5 minutes without having to look into the manuals again, while with dæmontools I had to check things every time I needed to change something. The tricky thing was the switch itself. It is a virtual server, presumably running in Xen, and I don’t have access to the console, so if I <s>bork</s> break something, I need to summon Bradley Kuhn or someone from [Conservancy](https://sfconservancy.org/), who’s kindly donated the server to the project. In any case, I decided to attempt to upgrade without a reboot, so that I have more options to roll back my changes in the case things go wrong.

After studying the manpages of both systemd’s `init` and sysvinit’s `init`, I realised I can install systemd as `/sbin/init` and ask already running System V init to re-exec. However, systemd’s `init` can’t talk to System V init, so before installing systemd I made a backup on it. It’s also important to stop all running services (except probably ssh) to make sure systemd doesn’t start second instances of each. And then: `/tmp/init u` — and we’re running systemd! A couple of additional checks, and it’s safe to reboot.

Only when I did all that I realised that in the case of systemd not working I’d probably not be able to undo my changes if my connection interrupted. So, even though at the end it worked, probably it’s not a good idea to perform such manipulations when you don’t have an alternative way to connect to the server :)

---
layout: post
title: Bye-bye binary vconfig(1)
date: 2019-01-02T13:01:00
lastmod: 2019-01-02T13:01:00
comments: true
tags: ["vlan", "vconfig", "Debian"]
slug: vlan-vconfig
---

This morning I have decided that this is the time. The time to finally remove the [binary vconfig utility](https://linux.die.net/man/8/vconfig) (which used to [help people configure VLANs](https://blog.sleeplessbeastie.eu/2012/12/23/debian-how-to-create-vlan-interface/)) from Debian. But fear not, the command isn’t going anywhere (yet), since almost six years ago I’ve written a [shell script](https://bugs.debian.org/501402#39) that replaces it, using `ip(8)` instead of the old and deprecated API.

If you’re still using vconfig, please give it a test and consider moving to better, newer ways of configuring your VLANs.

If you’re not sure whether you’re using it or not, mostly likely not only you aren’t, but it’s quite possible that you may not even need the [`vlan` package](https://tracker.debian.org/pkg/vlan) that ships vconfig, since the most important functionality of it has since been implemented in ifupdown, networkd and NetworkManager.

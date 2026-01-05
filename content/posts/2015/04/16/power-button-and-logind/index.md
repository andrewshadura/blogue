---
layout: post
title: "Power button and logind"
date: 2015-04-16T14:05:00
lastmod: 2015-04-16T14:05:00
comments: true
tags: []
---

If you have configured your laptop's power button to act as sleep button using `acpid`, then installed systemd or systemd-shim and pressed the button only to find your laptop to shut down after it wakes up from sleep, set these options in `/etc/systemd/logind.conf`:

    [Login]
    HandlePowerKey=ignore
    HandleSuspendKey=ignore
    HandleHibernateKey=ignore
    HandleLidSwitch=ignore

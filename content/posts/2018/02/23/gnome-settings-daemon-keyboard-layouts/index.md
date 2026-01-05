---
layout: post
title: "How to stop gnome-settings-daemon messing with keyboard layouts"
date: 2018-02-23T16:23:00
lastmod: 2018-02-23T16:23:00
comments: true
slug: gnome-settings-daemon-keyboard-layouts
tags: ["Debian", "Ubuntu", "GNOME", "Unity"]
---

In case you, just like me, want to have a heavily customised keyboard layout configuration, possibly with different layouts on different input devices (I recommend [inputplug](https://bitbucket.org/andrew_shadura/inputplug/) to make that work), you probably don’t want your desktop environment to mess with your settings or, worse, re-set them to some default from time to time. Unfortunately, that’s exactly what `gnome-settings-daemon` does by default in GNOME and Unity. While I could modify inputplug to detect that and undo the changes immediately, it turned out this behaviour can be disabled with an underdocumented option:

    gsettings set org.gnome.settings-daemon.plugins.keyboard active false

Thanks to [Sebastien Bacher](https://blogs.gnome.org/seb128/) for helping me with this two years ago.

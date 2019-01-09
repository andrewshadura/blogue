---
layout: post
title: wpa-supplicant and hostapd 2.7 in Debian
date: 2019-01-02 13:29
comments: true
tags: WPA supplicant, hostapd, Debian
slug: wpa-supplicant-2.7
---

Hostapd and wpa-supplicant 2.7 have been in Debian experimental for some time already, with snapshots available since [May 2018](https://packages.qa.debian.org/w/wpa/news/20180507T183422Z.html), and the official release since [3 December 2018](https://packages.qa.debian.org/w/wpa/news/20181203T190858Z.html). I’ve been using those 2.7 snapshots myself since May, but I do realise my x250 with an Intel Wi-Fi card is probably not the most representative example of hardware wpa-supplicant would often run on, so before I upload 2.7 to unstable, it would be great if more people tested it. So please try to install it [from experimental](https://packages.debian.org/source/experimental/wpa) and see if it works for your use cases. In the latest upload, I have enabled a bunch of new upstream features which previously didn’t exist or were still experimental, so it would be great to give them a go.

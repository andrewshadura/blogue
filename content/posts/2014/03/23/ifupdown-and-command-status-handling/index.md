---
layout: post
title: "ifupdown and command status handling"
date: 2014-03-23T18:31:00
lastmod: 2014-03-23T18:31:00
comments: true
tags: []
---

In 2011, I first tried to fix a [Debian bug #547587](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=547587). The bug was about hook script result codes not being checked, so if a script fails, this isn't detected. Unfortunately, just checking the return code wasn't enough, as lots of scripts didn't care about their return code at all, so I had to unapply the patch.

Now, after 2.5 years, I think it's time to try again, as most of the scripts have been fixed since then. At the same time, I've changed error handling a little bit further: errors in any commands or scripts during interface configuration are considered fatal, but when interface is deconfigured, errors are ignored. However, this may change break configurations which depend on previous behaviour.

Please report bugs if you find any.

---
layout: post
title: "Linux, snd_hda_intel and Sigmatel STAC9200"
date: 2012-09-05T23:35:00
lastmod: 2012-09-05T23:35:00
comments: true
slug: linux-snd-hda-intel-and-sigmatel-stac9200
tags: ["Linux"]
---

Strange and interesting thing has happened to me recently. I'm a user of Dell
D620 laptop, which has Intel's HDA controller and Sigmatel's STAC9200 codec.
This has always worked perfectly fine, and in my mixer I could see at least two
volume controls: Master and PCM. Changing volume using both worked.

Once I've upgraded my Linux 3.2 to 3.4, and have noticed that Master volume
control is no more. What's up I thought, but did nothing. Update to 3.5 hasn't
fixed the problem. Okay, it's time to ``bisect`` stuff.
<!-- more -->

Bisection has shown that this commit has introduced the change which affected
me:
<pre>
From 2faa3bf15ba69fa12bc53926b88982b3875abb3f Mon Sep 17 00:00:00 2001
From: Takashi Iwai <tiwai@suse.de>
Date: Mon, 12 Mar 2012 12:30:22 +0100
Subject: [PATCH] ALSA: hda - Rewrite the mute-LED hook with vmaster hook in patch_sigmatel.c

<…>

Also, this patch changes the code to create vmaster always even on
STAC9200 and STAC925x.  The former "Master" on these chips are renamed
as "PCM" now.

Signed-off-by: Takashi Iwai <tiwai@suse.de>

</pre>

That looks very strange, as it means there wasn't PCM volume control. And indeed,
compiling and loading kernel module from Linux 3.1 brings Master volume control
back, but PCM volume control disappears.

More over, when I looked up into the datasheet, I've found no mention of PCM
volume control there:

![](stac9200-1.png)

![](stac9200-2.png)

I don't understand how could that happen and how to solve this. I've mailed
Takashi on this regard, so probably he may tell me something.

*Update*: With a bit of my help, Takashi has solved the problem: https://lkml.org/lkml/2012/9/28/682

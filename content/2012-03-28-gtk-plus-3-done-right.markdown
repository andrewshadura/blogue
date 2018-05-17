---
layout: post
title: "GTK+ 3 done right"
date: 2012-03-28 13:02
comments: true
slug: gtk-plus-3-done-right
tags: 
---

Ever wanted your GTK+ 3 look better? Unsatisfied with the default settings of Adwaita theme?
Add these configuration files to your `~/.config/gtk-3.0`:

{% gist 2225446 gtk.css %}

This will add some nice borders to menus as well proper background to menu items.

{% gist 2225446 settings.ini %}

And this will set font to `Sans 9` and not anything else which is for some reason is the default.

---
layout: post
title: "Extra large image editing"
date: 2009-03-24 11:04
comments: true
tags: 
---

How often do you need to do something with extra-large images? Usually, I don't need to, but recently I've received one such an image, and really needed to crop it. That image was 21 MiB 16 Kpixel×12 KPixel aerial image in a JPEG file. As anybody knows, JPEG files can be converted without decoding the whole image in the memory, you can read [why](http://en.wikipedia.org/wiki/JPEG) on the Wikipedia. You just need to go through all image blocks sequentially and write them in the new format. If the image is progressive JPEG, this is even easier. The same with cropping: you can just skip some image blocks without decoding them.

I was surprised when discovered that my usual helper programs couldn't crop this file without eating all my memory and disk space (my laptop has limited both). ImageMagick's convert and couldn't do the task: convert got 795 MiB virt and 300 MiB res, and created 1.2 GiB temp file, so I killed it. nip2, while it was recommended by some people, wasn't able to work for some reason, it just couldn't load the image at all.

I was ready to write my own JPEG re-encoder when I've found [jpegtran](http://packages.debian.org/libjpeg-progs). It was written by [IJG](http://ijg.org/) (Independent JPEG Group). This program was able to do anything I needed. It can crop, flip, flop, rotate, transpose and transverse images, convert them to greyscale, re-optimize, and make JPEG progressive. Also you can control memory usage, so it will not make you system unresponsive by eating it all.

Cropping image is as easy as this:

``$ jpegtran -crop 640x480+0+0 in.jpg > out.jpg``

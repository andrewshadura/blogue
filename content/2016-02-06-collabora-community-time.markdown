---
layout: post
title: Community time at Collabora
date: 2016-02-06 18:22 +0100
updated: 2016-02-06 20:49 +0100
comments: true
tags: Collabora, Debian
image: http://blog.shadura.me/images/posts/sparkles.png
---

I haven't yet blogged about this (as normally I don't blog often), but I
joined [Collabora](https://www.collabora.com/) in June last year. Since then,
I had an opportunity to work with OpenEmbedded again, write a kernel patch,
learn lots of things about systemd (in particular, how to stop worrying about
it taking over the world and so on), and do lots of other things.

As one would expect when working for a free software consultancy, our customers
do understand the value of the community and contributing back to it, and so does the
customer for the project I'm working on. In fact, our customer
insists we keep the number of locally applied patches to, for example, Linux kernel, to
minimum, submitting as much as possible upstream.

However, apart from the upstreaming work which may be done for the customer, Collabora
encourages us, the engineers, to spend up to two hours weekly for upstreaming on top
of what customers need, and up to five days yearly as paid Community days. These
community days may be spent working on the code or doing volunteering at free software
events or even speaking at conferences.

Even though on this project I [have](https://anonscm.debian.org/cgit/collab-maint/ifupdown.git/commit/?id=da5ff47d42c094a913c01fbb27f7b9be60538d15)
[already](https://anonscm.debian.org/cgit/collab-maint/ifupdown.git/commit/?id=05ba6bf079516550eeea15210f39a82bbfb03cae)
[been](https://anonscm.debian.org/cgit/collab-maint/ifupdown.git/commit/?id=86c01dc85ae3042ad0ccc019dc10ffef3fbf6f74)
[paid](https://anonscm.debian.org/cgit/collab-maint/ifupdown.git/commit/?id=ba122e2c102fc4cdedac0dd2dd3695705c5f42ad)
for contributing to the free software project which I maintained in my free time previously (ifupdown),
paid community time is a great opportunity to contribute to the projects I'm interested in, and if
the projects I'm interested in coincide with the projects I'm working with, I effectively can spend even
more time on them.
<!-- more -->

A bit unfortunately for me, I haven't spent enough time last year to plan my community days, so I used most
of them in the last weeks of the calendar year, and I used them <ins datetime="2016-02-06T20:49:00+01:00">(and some of my upstreaming hours)</ins> on something that benefitted both free software
community and Collabora. I'm talking about [SparkleShare](http://sparkleshare.org/), a cross-platform Git-based
file synchronisation solution written in C#. SparkleShare provides an easy to use interface for Git, or, actually,
it makes it possible to not use any Git interface at all, as it monitors the working directory using inotify and
commits stuff right after it changes. It automatically handles conflicts even for binary files, even though I
have to admit its handling could still be improved.

<img src="/images/posts/sparkles.png" style="float: right;">

At Collabora, we use SparkleShare to store all sorts of internal documents, and it's being used by users not
familiar with command line interfaces too. Unfortunately, the version we [recently had](https://packages.qa.debian.org/s/sparkleshare/news/20151221T223515Z.html)
in Debian had a couple of very annoying bugs, making it a great pain to use it: it would not notice edits in
local files, or not notice new commits being pushed to the server, and that led to individual users' edits
being lost sometimes. Not cool, especially when the document has to be sent to the customer in a couple of
minutes.

The new versions, 1.4 (and recently released 1.5) was reported as being much better and also fixing some crashes,
but it also used GTK+ 3 and some libraries not yet packaged for Debian. [Thanh Tung Nguyen](https://launchpad.net/~rebuntu16)
packaged these packages (and a newer SparkleShare) for Ubuntu and published them in his [PPA](https://launchpad.net/~rebuntu16/+archive/ubuntu/sparkleshare+unofficial), but they required some work to be fit for Debian.

I have never touched Mono packages before in my life, so I had to
learn a lot. Some time was spent talking to upstream about fixing
their copyright statements (they had none in the code, and only
one author was mentioned in configure.ac, and nowhere else in the
source), a bit more time went into adjusting and updating the patches
to the current source code version. Then, of course, waiting the
packages to go through NEW. Fixing [parallel build issues](http://bugs.debian.org/810280),
waiting for buildds to all build dependencies for at least one architecture…
But then, finally, on 19<sup>th</sup> of January I had the [updated SparkleShare](https://packages.qa.debian.org/s/sparkleshare/news/20160119T093826Z.html)
in Debian.

As you may have already guessed, this blog post has been sponsored by
Collabora, the first of my employers to <del datetime="2016-02-06T20:49:00+01:00">encourage</del> require me to work on
free software in my paid time :)

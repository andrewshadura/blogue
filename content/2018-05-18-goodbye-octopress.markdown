---
title: "Goodbye Octopress, hello Pelican"
date: 2018-05-18 22:05
slug: goodbye-octopress
image: https://blog.shadura.me/images/posts/minidebconf-hamburg.jpg
comments: true
---

<img src="/images/posts/minidebconf-hamburg.jpg" class="img-responsive" style="max-width: 60%;">

Hi from MiniDebConf in Hamburg!

As you may have noticed, I don’t update this blog often. One of the reasons why this was
happening was that until now it was incredibly difficult to write posts. The software I
used, Octopress (based on Jekyll) was based on Ruby, and it required quite specific versions
of its dependencies. I had the workspace deployed on one of my old laptops, but when I attempted
to reproduce it on the laptop I currently use, I failed to. Some dependencies could not be installed,
others failed, and my Ruby skills weren’t enough to fix that mess. (I have to admit my Ruby skills
improved *insignificantly* since the time I installed Octopress, but that wasn’t enough to help in
this case.)

I’ve spent some time during this DebCamp to migrate to Pelican, which is written in Python, packaged
in Debian, and its dependencies are quite straighforward to install. I had to install (and write) a few
plugins to make the migration easier, and port my custom Octopress Bootstrap theme to Pelican.

I no longer include any scripts from Twitter or Facebook (I made *Tweet* and *Share* button static links),
and the Disqus comments are loaded only on demand, so reading this blog will respect your privacy better
than before.

See you at MiniDebConf tomorrow!

<img src="/images/posts/minidebconf-hamburg-debian.jpg" class="img-responsive" style="max-width: 60%;">

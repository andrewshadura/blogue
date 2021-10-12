---
layout: post
title: Making the blog part of the Fediverse and IndieWeb
date: Wed 30 Dec 20:07:03 CET 2020
comments: true
slug: blog-on-the-fediverse
tags: Fediverse, IndieWeb, microformats
---

I’ve just made my blog available on the Fediverse, at least partially.

Yesterday while browsing Hacker News, I saw [Carl Schwan](https://carlschwan.eu/)’s post <a href="https://carlschwan.eu/2020/12/29/adding-comments-to-your-static-blog-with-mastodon/">Adding comments to your static blog with Mastodon</a><sup>(<a href="https://linuxrocks.online/@carl/105463655803971969">m</a>)</sup> about him replacing Disqus with replies posted at Mastodon. Just on Monday I was thinking, why can’t blogs participate in Fediverse? I tried to use WriteFreely as a replacement for Pelican, only to find it very limited, so I thought I might write a gateway to expose the Atom feed using ActivityPub. Turns out, someone already did that: [Bridgy](https://brid.gy/), a service connecting websites to Twitter, Mastodon and other social media, also has a Fediverse counterpart, [Fed.brid.gy](https://fed.brid.gy/) — just what I was looking for!

I won’t go deeply into the details, but just outline issues I had to deal with:

* Bridgy relies on microformats. While I had some microformats and Schema.org microdata already at both blog and the homepage, they were not sufficiently good for Bridgy to use.
* Webmention: I had to set up <https://webmention.io> to act as Webmention host for me.
* I ran into an [issue](https://github.com/snarfed/bridgy-fed/issues/73) with Mastodon being more picky about signatures — which the author [% mention name="Ryan Barrett" url=https://snarfed.org/ %] promptly fixed.

The end result is not fully working yet, since posts don’t appear yet, but I can be found and followed as `@shadura.me@shadura.me`.

As a bonus I enabled [IndieAuth](https://indieauth.com/) at my website, so I can log into compatible services with just the URL of my website.

<a style="display: none;" href="https://brid.gy/publish/twitter"></a>
<a style="display: none;" href="https://brid.gy/publish/mastodon"></a>

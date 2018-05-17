---
layout: post
title: "Clearlooks-Phénix update"
date: 2014-02-05 22:58
comments: true
tags: 
---

Once upon a time, GTK+ 3.0 was released. That release brought at least one Bad Thing™:
incompatibility with GTK+ 2.x themes. At the same time, previously popular Clearlooks
theme hasn't been ported. Many people didn't like that, but only one decided to DTRT —
to do the Right Thing. Jean-Philippe Fleury wrote Clearlooks-Phénix (originally, Clearwaita),
a GTK+ 3 theme which was supposed to have a look and feel as close as possible to the
original Clearlooks. He based his work on an engine of a new GTK+ default, Adwaita theme.
Quite soon, however, GTK+ 3 theme API has changed, and it became easily possible to rewrite
the theme without using any additional theming engines, with just plain GTK+ stuff involved.

Then GTK+ 3.6 came and broke the API once more. Jean-Philippe fixed stuff to work with newer
GTK+ again, and everyone was happy again.

But Empire striked back: GTK+ 3.8 brought more disruptive changes, rendering menus
as ugly as never before. Unfortunately, Jean-Philippe was unable to cope with changes alone,
he set up a mailing list to collectively develop Clearlooks-Phénix, but that didn't help,
and no fix has been released during more than half a year.

As a maintainer and a user of Clearlooks-Phénix, I had to do something with this, as more and
more things needed recent GTK+ 3 to work. After spending some time studying CSS code and playing
with its knobs, I found a solution which proved to be quite simple, and uploaded an updated package.
Unfortunately, the changes aren't in the upstream package yet.

Now, with GTK+ 3.10, stuff is not quite working again. Some changes in GTK+ internals
lead to menu bars not being coloured properly. At the moment of this writing, an updated
package is already available in unstable.

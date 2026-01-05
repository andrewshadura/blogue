---
layout: post
title: "Binary watch: NG"
date: 2011-11-30T16:39:00
lastmod: 2011-11-30T16:39:00
comments: true
tags: []
---

LED binary watch is a one of the most common geek gadgets available. The only problem with binary watch is that while it's done to be 'cool' and unusual, it's also not very convenient to use even for geeks, at least in my opinion. I think so because it fundamentally breaks the way people use watch usually. Correct me if I am wrong, but in my opinion the exact numbers don't have any real meaning for everyone who uses watch. What's important is which part of some interval of time is now: morning, evening, noon or midnight, and a fraction which tells us how far we are from one important point in time or from another. The same applies to shorter time intervals: usually an hour's divided into quarters or 5-minute intervals.

So, I'd like to propose a different approach.

First, we divide twenty-four hours into intervals of 3 hours each, and encode this in binary. Thus, any time between 12:00 and 14:59 will be represented by a code `0100`. To specify the exact hour inside that interval, we append its number in binary to the code above, so for 13:00 we get `0100.01`. The code `.11` isn't used in this approach at all.

Next, the same we can do to minutes. Two digits can be used to specify an hour quarter. To specify the exact minute, we add four more digits; the code `.1111` isn't used again.

Now, some examples:

`12:34 → 12+00 : 30+04 → 0100.00 : 10.0100`

`03:27 → 03+00 : 15+12 → 0001.00 : 01.1100`

Anyone to produce such a binary watch? ;)

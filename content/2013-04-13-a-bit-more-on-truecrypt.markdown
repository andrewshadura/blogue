---
layout: post
title: "A bit more on TrueCrypt"
date: 2013-04-13 16:01
comments: true
tags: Debian
---

Few days ago I was discussing my last [blog post](/2013/01/05/truecrypt-ntfs-3g-loop/) with a colleague of mine, [Lukaš Tvrdý](https://plus.google.com/110593868562394816384/), and he's mentioned that it actually is possible to harmlessly decrypt the TrueCrypted filesystem in online mode, resize it, and encrypt it back again. Well, I decided to try, because I have had some problems with that setup. Apart from init script reordering I had to make (not covered in the post, as I did it later and haven't found time yet to write about that), I ran into a trouble while trying to enable swapping. As the only partition I had was formatted into NTFS, placing a swap file there isn't the best idea ever. I actually tried doing so, but after two deadlocks I had in few hours I had to rethink that. Indeed, as NTFS is implemented in the user space using ntfs-3g, as soon as this process gets swapped out, the system is left helpless. The swap is on the file system driver of which is in the swap, which is on the file system driver of which is... well, you get the idea.

Basically, I got rid of ext3-on-the-loop, and now I have real ext3 in a LUKS container, plus a separate swap partition. Now the other problem is: I still have an encrypted NTFS filesystem which I occasionally need to access, but I don't want to type the pass phrase twice... Something to think about.

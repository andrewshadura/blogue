---
layout: post
title: Transitioning to a new OpenPGP key
date: 2021-01-01T16:08:45
lastmod: 2021-01-01T16:08:45
comments: true
slug: new-openpgp-key
tags: ["Debian"]
---

Following {{< mention url=https://dkg.fifthhorseman.net/blog/author/daniel-kahn-gillmor.html name=dkg >}}’s [example](https://dkg.fifthhorseman.net/blog/2021-dkg-openpgp-transition.html), I decided to finally transition to my new `ed25519`/`cv25519` key.

Unlike Daniel, I’m not yet trying to split identities, but I’m using this chance to drop old identities I no longer use. My new key only has my main email address and the Debian one, and only those versions of my name I still want around.

My old PGP key (at the moment in the Debian keyring) is:
```
pub   rsa4096/0x6EA4D2311A2D268D 2010-10-13 [SC] [expires: 2021-11-11]
      782130B4C9944247977B82FD6EA4D2311A2D268D
uid                   [ultimate] Andrej Shadura <andrew@shadura.me>
uid                   [ultimate] Andrew Shadura <andrew@shadura.me>
uid                   [ultimate] Andrew Shadura <andrewsh@debian.org>
uid                   [ultimate] Andrew O. Shadoura <Andrew.Shadoura@gmail.com>
uid                   [ultimate] Andrej Shadura <andrewsh@debian.org>
sub   rsa4096/0xB2C0FE967C940749 2010-10-13 [E]
sub   rsa3072/0xC8C5F253DD61FECD 2018-03-02 [S] [expires: 2021-11-11]
sub   rsa2048/0x5E408CD91CD839D2 2018-03-10 [S] [expires: 2021-11-11]
```

The is the key I’ve been using in Debian from the very beginning, and its copies at the SKS keyserver network still have my first DD signature from {{< mention name=angdraug url=https://mastodon.social/@angdraug >}}:
```
sig  sig   85EE3E0E 2010-12-03 __________ __________ Dmitry Borodaenko <angdraug@mail.ru>
sig  sig   CB4D38A9 2010-12-03 __________ __________ Dmitry Borodaenko <angdraug@debian.org>
```

My new PGP key is:
```
pub   ed25519/0xE8446B4AC8C77261 2016-06-13 [SC] [expires: 2022-06-25]
      83DCD17F44B22CC83656EDA1E8446B4AC8C77261
uid                   [ultimate] Andrej Shadura <andrew@shadura.me>
uid                   [ultimate] Andrew Shadura <andrew@shadura.me>
uid                   [ultimate] Andrej Shadura <andrewsh@debian.org>
uid                   [ultimate] Andrew Shadura <andrewsh@debian.org>
uid                   [ultimate] Andrei Shadura <andrew@shadura.me>
sub   cv25519/0xD5A55606B6539A87 2016-06-13 [E] [expires: 2022-06-25]
sub   ed25519/0x52E0EA6F91F1DB8A 2016-06-13 [A] [expires: 2022-06-25]
```

If you signed my old key and are reading this, please consider signing my new key; if you feel you need to re-confirm this, feel free to contact me; otherwise, a copy of this statement signed by both the old and new keys is available [here]({attach}2021-01-01-new-openpgp-key.txt).

I have uploaded this new key to [keys.openpgp.org](https://keys.openpgp.org), and also published it through WKD and the SKS network. Both keys can also be downloaded from [my website](https://shadura.me/key.pgp).

<a style="display: none;" href="https://brid.gy/publish/twitter"></a>
<a style="display: none;" href="https://brid.gy/publish/mastodon"></a>
<a style="display: none;" href="https://fed.brid.gy/"></a>

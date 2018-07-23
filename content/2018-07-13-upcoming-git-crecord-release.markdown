---
title: Upcoming git-crecord release
date: 2018-07-13 13:10
slug: upcoming-git-crecord-release
comments: true
---

More than 1½ years since the first release of [git-crecord](https://github.com/andrewshadura/git-crecord), I’m preparing a big update. Not aware how exactly many people are using it, I neglected the maintenance for some time, but last month I’ve decided I need to take action and fix some issues I’ve known since the first release.

First of all, I’ve fixed a few minor issues with `setup.py`-based installer some users reported.

Second, I’ve ported a batch of updates from a another crecord derivative merged into Mercurial. That also brought some updates to the bits of Mercurial code git-crecord is using.

Third, long waited Python 3 support is here. I’m afraid at the moment I cannot guarantee support of patches in encodings other than the locale’s one, but if that turns out to be a needed feature, I can think about implementing it.

Fourth, missing staging and unstaging functionality is being implemented, subject to the availability of free time during the holiday :)

The project is currently hosted at GitHub: [https://github.com/andrewshadura/git-crecord](https://github.com/andrewshadura/git-crecord).

P.S. In case you’d like to support me hacking on git-crecord, or any other of my free software activities, you can tip my [Patreon account](https://www.patreon.com/andrewsh).

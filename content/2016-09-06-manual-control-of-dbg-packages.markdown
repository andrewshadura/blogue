---
layout: post
title: "Manual control of OpenEmbedded -dbg packages"
slug: manual-control-of-dbg-packages
date: 2016-09-06 14:28
comments: true
tags: Yocto, OpenEmbedded
---

In December last year, OpenEmbebbed [introduced automatic debug packages](http://lists.openembedded.org/pipermail/openembedded-core/2015-December/114162.html). Prior to that, you’d need to manually construct `FILES_${PN}-dbg` variable in your recipe. If you need to retain manual control over precisely what does into debug packages, set an undocumented `NOAUTOPACKAGEDEBUG` variable to `1`, the same way Qt recipe does:

    NOAUTOPACKAGEDEBUG = "1"
    FILES_${PN}-dev = "${includedir}/${QT_DIR_NAME}/Qt/*"
    FILES_${PN}-dbg = "/usr/src/debug/"
    FILES_${QT_BASE_NAME}-demos-doc = "${docdir}/${QT_DIR_NAME}/qch/qt.qch"

P.S. Knowing this would have saved me and my colleagues days of work.

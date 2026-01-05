---
layout: post
title: "Removing accounts from Android devices"
date: 2012-05-07T03:32:00
lastmod: 2012-05-07T03:32:00
comments: true
tags: []
---

It's a well-known problem that Android offers no easy way to completely remove
the primary Google account, at least sometimes.

Well, there's one not really easy for people not involved with computer stuff,
but at least it works.

Once you have `adb shell` working, you need to log into your Android device and type `sqlite3 /data/system/accounts.db`.
That's the place where accounts are actually stored. In that database, there are tables named `accounts`, `grants`
and `authtokens`. Those you need to clean up:

    SQLite version 3.5.9
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> select _id,name from accounts;
    1|user@gmail.com
    sqlite> delete from authtokens where accounts_id=1;
    sqlite> delete from grants where accounts_id=1;
    sqlite> delete from accounts where _id=1;
    sqlite> select _id,name from accounts;

After that it may be a good idea to restart the device, but I'm not sure it's really needed.

---
layout: post
title: "ifupdown news"
date: 2012-04-19 22:28
comments: true
tags: Debian
---
A new version of ifupdown has been uploaded to experimental yesterday, which
brings some important changes.
<!-- more -->

First of all, now it's possible to specify default values for various
interface configuration options. This eliminates the need of hard coding
of them in C source, as Ubuntu has been doing for some time. End users
are not affected by this change at all, of course.

Second, now ifup behaves differently when it's called with `--all` option.
Previously, that was causing all interfaces marked as 'auto' to be brought
up. Now, it does exactly the same if `--allow` option isn't used. Otherwise,
it brings up the interfaces which are declared to belong to a specified
class using allow-\* directive. In other words, 'auto' directive indeed
declares interface as belonging to a class 'auto', and the default class for
ifupdown is also 'auto', so when user runs `ifup -a` only those interfaces
are brought up.

Also, when called with `--all`, both ifup and ifdown now also call hook
scripts before doing anything and just after that. Specifically, before
bringing interfaces up, it calls pre-up scripts with a special interface
name and a special address family (which can't happen otherwise), and calls
post-up scripts after doing everything it needs. Same happens with ifdown,
but it calls different scripts, of course. This feature helps to avoid
manual parsing of `/etc/network/interfaces` and `/run/network/ifstate` as
mountnfs script did (and still does), for example. In theory, exactly none
of the existing scripts should be broken by this change. At least, I couldn't
find any of distribution-supplied scripts which could break. Also, Network
Manager already uses similar approach, so if anything can break, it's been
broken for a long time already.

One more change is related to the initscript. `/etc/init.d/ifupdown` is no
more. However, ifupdown now provides `/etc/init.d/networking` instead of
netbase. This means, the next version of netbase needs to drop it, and
also setting up Breaks relationship would be cool. The script itself has
been changed a bit. Apart from other things, now it supports `reload` command
properly, grabbing the current interfaces state and bringing those interfaces
back up. Also, `start` command now tries to bring up interfaces which are
specified with 'allow-hotplug' if they can be brought up.

Cool news for Ubuntu maintainers and everyone else interested: now ifupdown
supports ifquery interface previously available in Ubuntu only. It has some
bugs fixed, and now seems to work properly with mappings and already-up
interfaces.

Finally, `/run` transition has almost finished, so please if you opened any
related bugs, please test and report if they still need fixing.

Also, this version (with one more bug discovered while preparing this post
fixed) is going to be upload to unstable as soon as enough people test it
to be sure it's not going to Break Everything At All. In that upload, I
plan to temporarily unapply a controversial patch already discussed on 
debian-devel@ which changed the processing of hook scripts' return values.

Please do test and report any bugs you find.

And, of course, a short summary of the changes:

  * Prefer isc-dhcp-client to dhcp3-client (also closes: #422885).
  * Let dhclient fail when no lease can be acquired (Closes: #420784).
  * Raise command-line options priority over `/etc/network/interfaces`
    (Closes: #657743).
  * Prevent aliases and VLANs from putting the main interface down
    (Closes: #656270).
  * Make iproute2 calculate the broadcast address (LP: #924880).
  * Shut udhcpc down correctly (Closes: #338348).
  * Update the rules according to `/run` migration.
  * Pass hardening flags from dpkg-buildflags (Closes: #661243).
  * Implement ifquery interface (Closes: #568479).
    - Make ifquery process mappings (LP: #850166).
    - Ensure ifquery always has no\_act turned on.
  * Change `--all` behaviour:
    - If ifup or ifquery is called with the `--all` option, if doesn't just
      bring up all interfaces marked as "auto", but all interfaces of a
      specified class, "auto" by default. For the most uses, this doesn't
      change anything, but lets all the interfaces of a specific class to be
      brought up or queried.
  * Support cross-compilation, move Debian-specific things out of
    the Makefile (Closes: #666084).
  * Take networking init script over from netbase package.
    - Add reload action which reconfigures all interfaces currently
      configured.
    - Add LSB Description field.
    - Remove `/usr` from PATH.
    - Merge ifupdown initscript in.
    - Improve warning messages.
    - Don't use redirection hacks when parsing `/proc/mounts` and `/proc/swap`.
    - Document all supported subcommands.
    - On start, try to configure hotplug interfaces if they seem to be ready.
      Ignore errors if they fail to configure for some reason (for example,
      if the interface happens to be renamed by udev before it's fully
      configured).
    - Override Lintian's false positives.
  * Remove `/etc/default/ifupdown`.
  * Call hook scripts when processing all interfaces:
    - If ifupdown is called with the `--all` option, before or after doing
      anything to the interfaces, it calls all the hook scripts (pre-up or
      down) with IFACE set to "\-\-all", LOGICAL set to the current class
      specified by the `--allow` option (or "auto" if it's not set),
      ADDRFAM="meta" and METHOD="none".
  * Fix IPv6 issue on kFreeBSD.
  * Update test suite.
  * Improve manual pages.
  * Bump Standards-Version to 3.9.3.
  * Also closes: #535226:
    - In 0.7~alpha5, "auto" method has been added.

Also posted to debian-devel@ maillist.


---
layout: post
title: "How to run Debian from a loop device on a TrueCrypt'ed NTFS partition"
date: 2013-01-05T01:40:00
lastmod: 2013-01-05T01:40:00
comments: true
slug: truecrypt-ntfs-3g-loop
tags: []
---

After I have changed my job recently I had to meet the security policies which
are enforced in the company I'm now working for. First of all, I'm not allowed
to use my own laptop, and the company-provided laptop has Windows installed.
As my job is, unfortunately, not directly related to Linux, I'm not allowed to
re-install the OS. However, working in the comfortable environment is what I
really need to do my job effectively, so I have designed a workaround.
<!-- more -->

The workaround is, basically, to install Debian into an ext3 filesystem image,
which itself lies on an NTFS partition, which itself is encrypted using
TrueCrypt. Thus I keep Windows installation unharmed, while I'm still able to
run operating system of my choice, and to keep all the data encrypted, as
policies require. Also, to boot into Debian, I have to boot from the USB stick,
as I'm not sure I can install GRUB at the hard disk without doing any harm to
the fragile TrueCrypt + Windows boot loader duo.

Basically, what I needed to accomplish was the following:

* Boot Linux, map the encrypted partition using ``tcplay`` and ``device-mapper``.
* Mount the NTFS filesystem using ``ntfs-3g``.
* Mount the ext3 filesystem image using a loop device.
* Move the NTFS mountpoint to the new filesystem root.
* Switch to the new filesystem root.

Everything above is performed from initramfs, thus giving an opportunity to
do that smoothly and to let the USB stick be used to boot the kernel only.

I don't really know how initramfs manipulations are done in distributions other
than Debian, but at least in Debian there's a framework which allows few hook scripts to
be placed under ``/etc/initramfs-tools``, so on the initramfs rebuild some new stuff
may be pulled in.

First of all, we want ``tcplay``, which is a free implementation of TrueCrypt,
to be available in initramfs. For that, we put the following file under
``/etc/initramfs-tools/hooks``:

**`tcplay.sh`:**

```bash
#!/bin/sh

set -e

PREREQ="dmsetup"

prereqs () {
        echo "${PREREQ}"
}

case "${1}" in
        prereqs)
                prereqs
                exit 0
                ;;
esac

. /usr/share/initramfs-tools/hook-functions

copy_exec /usr/bin/tcplay /bin

manual_add_modules dm_crypt

copy_modules_dir kernel/crypto

exit 0
```

Here, we first require ``dmsetup`` to be installed into initramfs, as we depend
on it. Then we copy ``tcplay`` itself, and then add module required by it. I've
decided to add all cryptomodules, as I don't know which exactly of them
TrueCrypt may require.

Also, as TrueCrypt is going to request a pass phrase, we need to ensure it gets
access to the console input. I know this is definitely not the best way to
accomplish this, but it was the easiest way I managed to find that worked: to
use ``openvt`` utility from ``console-tools`` package. The following file goes
to the same directory as the previous one:

**`console-tools.sh`:**

```bash
#!/bin/sh

set -e

PREREQ=""

prereqs () {
        echo "${PREREQ}"
}

case "${1}" in
        prereqs)
                prereqs
                exit 0
                ;;
esac

. /usr/share/initramfs-tools/hook-functions

copy_exec /usr/bin/openvt /bin

exit 0
```

At this point, we have prepared all the required binaries. Now it's time to add
scripts to actually perform the filesystem manipulations.

The first step is to map the encrypted block device. We need to do that before
the root filesystem is mounted, so we put the following script into ``/etc/initramfs-tools/scripts/init-premount``:

**`tcplay-local.sh`:**

```bash
#!/bin/sh

set -e

case "${1}" in
        prereqs)
                exit 0
                ;;
esac

openvt -c 1 -f -w -s tcplay -m winroot -d /dev/disk/by-id/ata-YOUR-DISK-ID-part2 -s /dev/disk/by-id/ata-YOUR-DISK-ID

exit 0
```

``openvt`` attaches ``tcplay`` to the VT1 and waits for it to get the pass phrase from user.
As the result, the unencrypted block device becomes seen as ``/dev/mapper/winroot``.

Next thing is to mount the NTFS partition:

**`ntfs-mount.sh`:**

```bash
#!/bin/sh

set -e

case "${1}" in
        prereqs)
                echo tcplay-local.sh
                exit 0
                ;;
esac

sleep 2
mkdir -p /media/winroot

ntfs-3g /dev/mapper/winroot /media/winroot

exit 0
```

This goes to the same directory. Note that we declare the dependency on ``tcplay-local.sh``.

After we've done that, the root filesystem can be mounted by the usual initramfs script, the 
only thing we need to do is to tell it how to mount it and where does it find it. It's done by
adding this to the kernel command line:

<pre>root=/media/winroot/rootfs rootflags=loop rootfstype=ext3</pre>

Of course, your filesystem image should be at ``/media/winroot/rootfs``.

After we have mounted the root filesystem, it may be a good idea to make the underlying NTFS
available for the user; if we don't move the mount point under the new root, it becomes
inaccessible later. This script goes into ``/etc/initramfs-tools/scripts/init-bottom``:

**`mount-move.sh`:**

```bash
#!/bin/sh

set -e

case "${1}" in
        prereqs)
                echo udev
                exit 0
                ;;
esac

# move the /media/winroot directory to the rootfs
mount -n -o move /media/winroot ${rootmnt}/media/winroot

# create a temporary symlink
nuke /media/winroot
ln -s ${rootmnt}/media/winroot /media/winroot

exit 0
```

It doesn't check for existance of ``/media/winroot`` mountpoint in the new root directory, so
you should create it beforehand, as at this point the root filesystem is mounted read-only.

Basically, this is enough to make system boot. However, there's a problem at shutdown:
``sendsigs`` initscript first terminates and then kills the ``ntfs-3g`` driver, so
the root filesystem stays unsynchronised and isn't cleanly unmounted. Originally, to solve
this I came up with my own custom init script, but apparently there's an easier way. ``sendsigs``
consults ``/run/sendsigs.omit.d`` directory for PID files of processes it shouldn't kill.
On the other hand, ``ntfs-3g`` provides an initramfs script which puts a PID of ``ntfs-3g``
process into this directory **if** the root filesystem is on NTFS, or if ``LOOPFSTYPE`` variable
says ``ntfs`` or ``ntfs-3g``. So it should be enough to place a file into ``/etc/initramfs-tools/conf``:

<pre>LOOPFSTYPE=ntfs-3g</pre>

Finally, to regenerate the initramfs, run ``update-initramfs -k all -u`` and copy it to your bootable medium.

Well, test, enjoy using this (if you need to), report bugs!


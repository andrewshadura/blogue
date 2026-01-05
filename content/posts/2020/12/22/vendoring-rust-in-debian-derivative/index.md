---
layout: post
title: Vendoring Rust dependencies for a Debian derivative
date: 2020-12-22T19:26:57
lastmod: 2020-12-22T19:26:57
comments: true
slug: vendoring-rust-in-debian-derivative
tags: ["Rust", "Debian"]
---

Recently, I needed to package a [Rust crate `libslirp`][libslirp-rs] for a [Apertis, a Debian derivative][Apertis]. `libslirp` is used by the newly release UML backend of [debos][], our Debian image build tool. Unfortunately, this crate hasn’t yet been properly packaged for Debian proper, so I could not simply pull the packaging from Debian. Even worse, its build dependencies haven’t all been packaged yet. Most importantly, I have only uploaded [zbus][] to Debian today, and at that time none of its dependencies were in Debian either.

Another issue with this were that each crate is packaged for Debian as a separate package, making the process a bit more tricky since I’d need to import all of the crates into Apertis separately. Doing that takes time and is further complicated by the CI loop we’re using which requires the full build process to complete for a package before a pipeline a dependent package can run.

Having all that considered, I took a shortcut: I vendored all the build dependencies with the package itself, and here’s how.

I started with [debcargo-conf][], where the not-yet-complete packaging lives. With `debcargo`, I generated the source package as if I were to upload to Debian. Since I’ll be vendoring the dependencies, I have removed most of the Rust dependencies and replaced them with those extra dependencies needed by those crates.
So, I replaced this:

    Build-Depends: debhelper (>= 12),
     dh-cargo (>= 24),
     cargo:native,
     rustc:native,
     libstd-rust-dev,
     librust-enumflags2-0.6+default-dev (>= 0.6.4-~~),
     librust-ipnetwork-0.17+default-dev,
     librust-lazy-static-1+default-dev (>= 1.4-~~),
     librust-libc-0.2+default-dev,
     librust-libslirp-sys-4+default-dev (>= 4.2.0-~~),
     librust-libsystemd-0.2+default-dev,
     librust-mio-0.6+default-dev,
     librust-mio-extras-2+default-dev (>= 2.0.5-~~),
     librust-nix-0.17+default-dev,
     librust-slab-0.4+default-dev,
     librust-structopt-0.3+default-dev,
     librust-url-2+default-dev (>= 2.1-~~),
     librust-zbus-1+default-dev,
     librust-zvariant-2+default-dev

By this:

    Build-Depends: debhelper (>= 12),
     dh-cargo (>= 17),
     cargo:native,
     rustc:native,
     libstd-rust-dev,
     pkg-config,
     libglib2.0-dev,
     libslirp-dev

I wanted to keep the delta to the future Debian package at a bare minimum, so I kept the original `dh-cargo` build process, only making sure the vendored dependencies are found in the right place. The cleanest approach in my view was to use the fact that the `3.0 (quilt)` source format allows multiple original tarballs: the main tarball would be the same orig tarball as in Debian, and an extra tarball would contain the vendored code. When we sync with Debian, the extra tarball would be dropped, just as the adjustments to the `debian/rules`.

To generate the vendor tarball, I added this to the rules file:

```make
include /usr/share/dpkg/pkg-info.mk

vendor:
        -[ -d vendor ] && rm -rf vendor
        rm -rf Cargo.lock
        cargo vendor
        tar Jcf ../$(DEB_SOURCE)_$(DEB_VERSION_UPSTREAM).orig-vendor.tar.xz vendor/

.PHONY: vendor
```

This target, being run manually and not as part of the build process, download the latest dependencies satisfying the requirements in `Cargo.toml` and rolls them into a vendor tarball.

Now, to make `dh-cargo` use the vendored code, we need to link it into the right place. `dh-cargo` creates a Cargo registry tree in a subdirectly under `debian/` where it symlinks crates from the Rust development packages. This extra code makes sure the vendored dependencies are available there too:

```make
override_dh_auto_configure:
        dh_auto_configure $@
        for d in vendor/* ; \
        do \
                [ -L debian/cargo_registry/$$(basename $$d) ] && rm debian/cargo_registry/$$(basename $$d) ; \
                ln -rs $$d debian/cargo_registry ; \
        done
```

An important thing here is that if the build happens on a non-clean system, `dh-cargo` may have symlinked a system crate already installed — so we need to remove that symlink and replace it by ours. We build packages in clean chroots, so this is not that important, otherwise for reproducibility reasons it would be better to create the registry directory from scratch.

The final package can be found at the [Apertis GitLab](https://gitlab.apertis.org/pkg/rust-libslirp).

[Apertis]: https://www.apertis.org/
[libslirp-rs]: https://crates.io/crates/libslirp
[zbus]: https://crates.io/crates/libslirp
[debos]: https://github.com/go-debos/debos
[debcargo-conf]: https://salsa.debian.org/rust-team/debcargo-conf

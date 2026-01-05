---
layout: post
title: "GTK+ 3 done right"
date: 2012-03-28T13:02:00
lastmod: 2012-03-28T13:02:00
comments: true
slug: gtk-plus-3-done-right
tags: []
---

Ever wanted your GTK+ 3 look better? Unsatisfied with the default settings of Adwaita theme?
Add these configuration files to your `~/.config/gtk-3.0`:

**`gtk.css`:**

```css
.menu {
    border-style: solid;
    border-width: 1;
}

.menubar .menuitem *:prelight,
.menubar .menuitem:prelight {
    background-color: @theme_selected_bg_color;
    color: @theme_selected_fg_color;
}
```

This will add some nice borders to menus as well proper background to menu items.

**`settings.ini`:**

```ini
[Settings]
gtk-theme-name = Adwaita
gtk-fallback-icon-theme = gnome
gtk-font-name = Sans 9
```

And this will set font to `Sans 9` and not anything else which is for some reason is the default.

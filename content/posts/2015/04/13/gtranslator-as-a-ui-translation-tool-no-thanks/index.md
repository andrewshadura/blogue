---
layout: post
title: "UI translation tools and version control"
date: 2015-04-13T15:59:00
lastmod: 2015-04-13T15:59:00
comments: true
slug: gtranslator-as-a-ui-translation-tool-no-thanks
tags: []
---

Today I decided to try some translation tools I could install on my laptop locally
to translate [Kallithea](https://kallithea-scm.org/), so I'd not need to be on-line
to use Michal Čihař's wonderful [Weblate](https://weblate.org/).

The first tool I tried was [Gtranslator](https://wiki.gnome.org/Apps/Gtranslator). I edited about 5 strings, and then wanted
to commit my changes. To my surprise, the diff was huge. Apart from obvious changes
in the file header, like changing the team address or X-Generator field, Gtranslator
has reformatted almost every other entry in the file, adding meaningless line breaks
or reflowing the strings I didn't edit.

<pre>
@@ -3092,8 +3093,8 @@ msgstr ""
 
 #: kallithea/templates/admin/permissions/permissions_globals.html:72
 msgid ""
-"Write permission to a repository group allows creating repositories "
-"inside that group."
+"Write permission to a repository group allows creating repositories inside "
+"that group."
 msgstr ""
 
 #: kallithea/templates/admin/permissions/permissions_globals.html:77
</pre>

Apart from that it has quite a dumb user interface, so I most probably won't ever use it
again unless things improve.

Well, I thought, I need to try [Lokalize](https://userbase.kde.org/Lokalize) which I understand
is a Qt4 port of KBabel, which I remember was quite a reasonable translation tool.

Just as with Gtranslator, I created a project, edited one line and hit ‘Save’. As I expected,
Lokalize updated the file header, and also changed the formatting of some entries, though the
number of changes was significantly lower.

Yet the winner of this competition is Weblate, which indeed avoids unnecessary changes as much
as it can, just as advertised. Probably, I'll just stick with it, setting up a local instance.

# -*- coding: utf-8 -*-
"""
Some ActivityStreams features in the Atom feed.

Based on some ideas from Feed Filter plugin for Pelican by
David Alfonso <developer@davidalfonso.es> though very little
of the code survives; some pieces come from feedgenerator by
Django Software Foundation and Dirk Makowski.

Original code licensed as AGPL-3.0, new code under BSD-3-Clause license:

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials
    provided with the distribution.

 3. Neither the name of Django nor the names of its contributors
    may be used to endorse or promote products derived from this
    software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from datetime import datetime
from fnmatch import fnmatch
from logging import warning
from urllib.parse import urlparse

from pelican import signals, writers
from pelican.settings import DEFAULT_CONFIG

import feedgenerator
from feedgenerator import rfc3339_date

OrigAtom1Feed = feedgenerator.Atom1Feed

class ActivityStreamsAtom1Feed(OrigAtom1Feed):
    def root_attributes(self):
        attr = super().root_attributes()
        attr['xmlns:activity'] = 'http://activitystrea.ms/spec/1.0/'
        return attr

    def add_root_elements(self, handler):
        handler.addQuickElement("title", self.feed['title'])
        handler.addQuickElement("link", "", {"rel": "alternate", "href": self.feed['link']})
        handler.addQuickElement("link", "", {"rel": "hub", "href": "https://bridgy-fed.superfeedr.com/"})
        if self.feed['feed_url'] is not None:
            handler.addQuickElement("link", "", {"rel": "self", "href": self.feed['feed_url']})
        handler.addQuickElement("id", self.feed['id'])
        handler.addQuickElement("updated", rfc3339_date(self.latest_post_date()))
        if self.feed['author_name'] is not None:
            handler.startElement("author", {})
            handler.addQuickElement("activity:object-type", "http://activitystrea.ms/schema/1.0/person")
            handler.addQuickElement("name", self.feed['author_name'])
            if self.feed['author_email'] is not None:
                handler.addQuickElement("email", self.feed['author_email'])
            if self.feed['author_link'] is not None:
                handler.addQuickElement("uri", self.feed['author_link'])
            handler.endElement("author")
        if self.feed['subtitle'] is not None:
            handler.addQuickElement("subtitle", self.feed['subtitle'])
        for cat in self.feed['categories']:
            handler.addQuickElement("category", "", {"term": cat})
        if self.feed['feed_copyright'] is not None:
            handler.addQuickElement("rights", self.feed['feed_copyright'])


    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        handler.addQuickElement("activity:verb", "http://activitystrea.ms/schema/1.0/post")
        handler.addQuickElement("activity:object-type", "http://activitystrea.ms/schema/1.0/article")


def register():
    """Signal registration."""
    signals.initialized.connect(initialized)
    writers.Atom1Feed = ActivityStreamsAtom1Feed
    signals.feed_generated.connect(filter_feeds)


def initialized(pelican):
    DEFAULT_CONFIG.setdefault("AUTHOR_FULL_URL", None)
    if pelican:
        pelican.settings.setdefault("AUTHOR_FULL_URL", None)


def filter_feeds(context, feed):
    if not feed.feed['author_name']:
        feed.feed['author_name'] = context.get('AUTHOR')
    if not feed.feed['author_link']:
        feed.feed['author_link'] = context.get('AUTHOR_FULL_URL') or context.get('AUTHOR_URL')
    for item in feed.items:
        if not item['author_link']:
            item['author_link'] = context.get('AUTHOR_FULL_URL') or context.get('AUTHOR_URL')

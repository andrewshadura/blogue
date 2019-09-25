#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andrej Shadura'
SITENAME = 'Andrej\u2019s notes'
SITEURL = 'https://blog.shadura.me'

PATH = 'content'

THEME = 'theme'

CSS_FILE = 'style.css'

TIMEZONE = 'Europe/Bratislava'

DEFAULT_LANG = 'en'

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TWITTER_USER = 'andrew_shadura'

FACEBOOK_ID = '100000762850662'

DISQUS_SITENAME = 'andrewsh'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS = ['md-metayaml', 'liquid_tags.gist']

MENUITEMS = (('Blog', '/'),
             ('Archives', '/archives'),
             ('Photos', 'http://photos.shadura.me'),
             ('Panoramas', 'https://pano.shadura.me'),
             ('About me', 'https://shadura.me'))

DEFAULT_PAGINATION = 10

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

FEED_DOMAIN = SITEURL

DIRECT_TEMPLATES = ['index', 'categories', 'archives']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

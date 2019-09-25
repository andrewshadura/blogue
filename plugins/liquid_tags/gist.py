"""
Generic Tag
-----------
This implements a tag that that is mostly useful for testing.

This tag does not implement anything useful, but is a place that can be
used for testing liquid_tags infrastructure, in situations that need
a full lifecycle test.

The first use case is a test of a tag that will pull out data from
the configuration file and make it available during the test.

A tag of
{% gist config <config file variable> %>
will be replaced with the value of that config file in html

Not all config file variables are exposed - the set
of variables are from the LIQUID_CONFIGS setting, which is a list of 
variables to pass to the liquid tags.
"""
from .mdx_liquid_tags import LiquidTags

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import os
import sys
import io

from .include_code import include_code

def gist_url(gid):
    return 'https://gist.github.com/%s' % gid

def raise_error(fp, url):
    print('FAILED TO FETCH:', url)
    print('   status code:', fp.getcode())
    print('   response:')
    try:
        print(fp.read())
    finally:
        raise SystemExit()


def resolve_gid(gid):
    url = gist_url(gid)
    fp = urlopen(url)
    if fp.getcode() != 200:
        raise_error(fp, url)
    host, user, gid = fp.geturl().rsplit('/', 2)
    return "%s/%s" % (user, gid)

def fetch(gid, filename, typ):
    if not os.path.exists('.gists'):
        os.mkdir('.gists')
    key = os.path.join('.gists', ("%s/%s/%s" % (typ, gid, filename)).replace('/', ';'))
    if os.path.isfile(key):
        print('LOAD-CACHED:', key)
        return io.open(key, encoding='utf8').read()
    else:
        if typ == 'gist':
            gid = resolve_gid(gid)
            url = 'https://gist.githubusercontent.com/%s/raw/%s' % (gid, filename)
        elif typ == 'github':
            url = 'https://raw.githubusercontent.com/%s/%s' % (gid, filename)
        else:
            raise RuntimeError(typ)
        print('FETCHING:', url)
        fp = urlopen(url)
        if fp.getcode() != 200:
            raise_error(fp, url)
        data = fp.read()
        with open(key, 'wb') as fh:
            fh.write(data)
        return data.decode('utf8')

@LiquidTags.register('gist')
def gist(preprocessor, tag, markup):
    (gid, filename) = markup.split(' ', 2)
    lang = None
    text = fetch(gid, filename, 'gist')
    url = gist_url(gid)

    open_tag = ("<figure class='code'>\n<figcaption><span>{title}</span> "
                "<a href='{url}'>download</a></figcaption>".format(title=filename,
                                                                   url=url))
    close_tag = "</figure>"

    # store HTML tags in the stash.  This prevents them from being
    # modified by markdown.
    open_tag = preprocessor.configs.htmlStash.store(open_tag)
    close_tag = preprocessor.configs.htmlStash.store(close_tag)

    if lang:
        lang_include = ':::' + lang + '\n    '
    else:
        lang_include = ''

    if sys.version_info[0] < 3:
        source = (open_tag
                  + '\n\n    '
                  + lang_include
                  + '\n    '.join(text.decode('utf8').split('\n')) + '\n\n'
                  + close_tag + '\n')
    else:
        source = (open_tag
                  + '\n\n    '
                  + lang_include
                  + '\n    '.join(text.split('\n')) + '\n\n'
                  + close_tag + '\n')

    return source

#----------------------------------------------------------------------
# This import allows image tag to be a Pelican plugin
from liquid_tags import register


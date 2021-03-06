#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Creating reStructuredText Directives
# @see http://docutils.sourceforge.net/docs/howto/rst-directives.html
from docutils.parsers.rst import directives, Directive
from docutils import nodes

from pelican import signals
_CONTENT_PATH = None
_DEBUG = False

from os.path import basename
from os.path import join


ad1st = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 1st ad (upper) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="7078909202"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad2nd = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 2nd ad (middle) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="6133239602"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad3rd = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 3rd ad (below) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="6238827600"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad4th = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 4th ad (extra) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="2320208406"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad5th = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 5th ad (extra) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="5273674806"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

ad6th = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 6th ad (extra) - siongui.github.io -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0436733829999264"
     data-ad-slot="3354459609"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

class embed_adsense_code(Directive):
  required_arguments = 1
  has_content = False

  def run(self):
    sel = self.arguments[0].strip()
    html = ""
    if sel == "1":
      html = ad1st
    if sel == "2":
      html = ad2nd
    if sel == "3":
      html = ad3rd
    if sel == "4":
      html = ad4th
    if sel == "5":
      html = ad5th
    if sel == "6":
      html = ad6th

    return [nodes.raw('', html, format='html')]


def init_adsense_plugin(pelican_obj):
  global _CONTENT_PATH
  if _CONTENT_PATH is None:
    _CONTENT_PATH = pelican_obj.settings['PATH']


def register():
  signals.get_generators.connect(init_adsense_plugin)
  directives.register_directive('adsu', embed_adsense_code)

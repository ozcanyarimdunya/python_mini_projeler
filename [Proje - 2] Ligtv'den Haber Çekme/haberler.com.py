# coding=utf-8
"""
    <span class="divlinkA">Ülkenin Volkan'a İhtiyacı Var"</span>
    <span class="spotlink">Röportajın çarşamba günü yayınlanan ilk bölümü sizler tarafından büyük ilgi gördü.</span>
"""

import urllib
import re

site = urllib.urlopen('http://www.haberler.com/rss').read()

regex_hb = '<span class="spotlink">(.*)</span><span class="hbretkt"'
r_haber_basligi = re.compile(regex_hb)
for i in re.findall(r_haber_basligi, site):
    print i
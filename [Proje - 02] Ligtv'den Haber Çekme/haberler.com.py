# coding=utf-8
"""
    <span class="divlinkA">Ülkenin Volkan'a İhtiyacı Var"</span>
    <span class="spotlink">Röportajın çarşamba günü yayınlanan ilk bölümü sizler tarafından büyük ilgi gördü.</span>
"""

import re
import urllib.request

site = urllib.request.urlopen('http://www.haberler.com/rss').read().decode('utf-8')

regex_hb = r'<span class="spotlink">(.*)</span><span class="hbretkt"'
r_haber_basligi = re.compile(regex_hb)
for i in re.findall(r_haber_basligi, site):
    print(i)

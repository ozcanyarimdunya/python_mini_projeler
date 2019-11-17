#!/usr/bin/python3
# -*- coding: utf-8 -*-

import feedparser

"""
    cnn'den son dakika haberlerini çekme
"""
url = "http://www.cnnturk.com/feed/rss/news"
haberler = feedparser.parse(url)

i = 0
for haber in haberler.entries:
    i += 1
    print(i)
    print(haber.title)
    print(haber.link)
    print(haber.summary)
    print("\n")

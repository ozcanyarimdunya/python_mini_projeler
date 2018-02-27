# coding=utf-8
"""
    beautifulsoup ile bir siteden veri çekme
"""

import urllib.request

from bs4 import *

"""
 req = urllib.request.Request('http://www.python.org/fish.html')
>>> try:
>>>     urllib.request.urlopen(req)
>>> except urllib.error.HTTPError as e:
>>>     print(e.code)
>>>     print(e.read())

"""

headers = {'user_agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
req = urllib.request.Request(url="http://yusufcakmak.com", headers=headers)

html = urllib.request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(html)

basliklar = soup.findAll("h2", {"class": "post_title"})

for a, i in enumerate(basliklar):
    print(a + 1, i.next.next, i.a['href'])

# coding=utf-8
"""
    beautifulsoup ile bir siteden veri çekme
"""

import requests

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
url="http://yusufcakmak.com"

html = requests.get(url, headers=headers).content.decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

basliklar = soup.findAll("h2", {"class": "bwp-post-title entry-title"})

for a, i in enumerate(basliklar):
    print(a + 1, i.a.text, i.a['href'])

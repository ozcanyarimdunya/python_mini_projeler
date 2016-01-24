# coding=utf-8
"""
    beautifulsoup ile bir siteden veri çekme
    yusuf çakmak kimdir bilmiyorum hakkını helal et hocam :)
"""

from BeautifulSoup import *
import urllib

url = "http://yusufcakmak.com/"

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

basliklar = soup.findAll("h2", {"class": "post_title"})

for a, i in enumerate(basliklar):
    print a+1, i.next.next, i.a['href']

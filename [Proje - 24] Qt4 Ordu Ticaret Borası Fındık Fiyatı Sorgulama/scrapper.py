from __future__ import print_function

"""
    base_url = http://www.ordutb.org.tr/findik?date=2016-08-29&secenek=gun#fiyat_sorgula
"""
import urllib

from BeautifulSoup import *


class Scrapper:
    def __init__(self, year, month, day):
        if month < 10:
            self.month = "0" + str(month)
        else:
            self.month = str(month)

        if day < 10:
            self.day = "0" + str(day)
        else:
            self.day = str(day)

        self.year = year
        self.URL = "http://www.ordutb.org.tr/findik?date=" + str(
            self.year) + "-" + self.month + "-" + self.day + "&secenek=gun#fiyat_sorgula"
        self.soup = BeautifulSoup(urllib.urlopen(self.URL))

    def getPrice(self):
        a = []
        for i in self.soup.findAll("td"):
            for j in i:
                a.append(j)
        if len(a) == 1:
            return a[0]
        else:
            return a[1]+" : "+a[3]


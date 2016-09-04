from __future__ import print_function

"""
    base_url = http://www.ordutb.org.tr/findik?date=2016-08-29&secenek=gun#fiyat_sorgula
"""
import urllib

from BeautifulSoup import *


class Scrapper:
    def __init__(self, year, month, day):
        if month < 10:
            month = "0" + str(month)

        if day < 10:
            day = "0" + str(day)

        url = "http://www.ordutb.org.tr/findik?date=" + str(year) + "-" + str(month) + "-" + str(
            day) + "&secenek=gun#fiyat_sorgula"

        self.soup = BeautifulSoup(urllib.urlopen(url))

    def getPrice(self):
        data = []
        for i in self.soup.findAll("td"):
            for j in i:
                data.append(j)
        if len(data) > 1:
            return data[1] + " : " + data[3]
        else:
            return data[0]

# coding=utf-8

from __future__ import print_function

import urllib

from BeautifulSoup import *

"""

Kredi Tutarı(ktu)
Vade(v)
Faiz Oranı(f)
Ödeme Sıklığı(s)
Kredi Türü(krediTuru)
    Masrafsız Tüketici Kredisi              G1
    Tüketici Kredisi                        G11
    İpotekli Bireysel Finansman Kredisi     G12
    Biz Tüketici Kredisi                    G17
    Biz Masrafsız Tüketici Kredisi          G18
    Çalışan Biz Tüketici Kredisi            G24
    Çalışan Biz Masrafsız Tüketici Kredisi  G25
    Emekli Biz Tüketici Kredisi             G27
    Emekli Biz Masrafsız Tüketici Kredisi   G28
    Oyak Üyelerine Özel Tüketici Kredisi    G30
    Arsa Kredisi                            G5
    Eğitim Kredisi                          G6

# url = http://www.ziraatbank.com.tr/_layouts/ziraat/app_pages/_sp_hesapGrid.aspx?krediTuru=G1&ktu=5000&v=7&f=1,63&s=1


"""

BASE_URL = "http://www.ziraatbank.com.tr/_layouts/ziraat/app_pages/_sp_hesapGrid.aspx?"


class Scrapper:
    def __init__(self, kt, ktu, v, f, s):
        self.s = s
        self.v = v
        self.ktu = ktu
        self.kt = kt
        self.f = f
        url = "kt={}&ktu={}&v={}&f={}&s={}".format(kt, ktu, v, f, s)
        self.soup = BeautifulSoup(urllib.urlopen(BASE_URL + url))

    def getTable(self):
        table = []
        val = {}
        values = {}
        for c, tr in enumerate(self.soup.findAll("tr", {"class": re.compile("odd|even")})):
            td = tr.findAll("td", {"align": "center"})
            val["Sira"] = td[0].string
            val["Taksit"] = td[1].string
            val["Anapara"] = td[2].string
            val["Faiz"] = td[3].string
            val["KKDF"] = td[4].string
            val["BSMV"] = td[5].string
            val["Bakiye"] = td[6].string
            values[c] = val.copy()

        table.append(values)
        return table
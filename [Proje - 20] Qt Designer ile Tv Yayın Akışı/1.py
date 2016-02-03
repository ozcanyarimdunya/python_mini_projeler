#!/usr/bin/env python
# coding=utf-8
"""
    Proje 18 Çektiğimiz yayın akışlarını görsel bir ekrana atalım dedim
    İyi demiş miyim :)
    Bu aslında başlı başına bir olay öğrenmek için çok çaba sarfettim
    İnşallah faydalı olmuştur .
    Qt4 designer kurmanız gerekecektir
    sudo apt-get install python-qt4 demeniz yeterli olacaktır
"""
from __future__ import division

import sys
import urllib
import re

from BeautifulSoup import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.combo = QComboBox()
        self.combo.addItems(
            ["Kanal Seçin..".decode('utf-8'),
             "Kanal D",
             "Fox Tv",
             "Show Tv",
             "Star Tv",
             "Atv",
             "Trt 1",
             "Tv8",
             "Kanal 7",
             "A Haber",
             "CNN Turk",
             "CNBC-e",
             "Kanalturk",
             "Samanyolu",
             "Ntv",
             "TNT",
             "Halk Tv",
             "GS Tv",
             "FB Tv",
             "BJK Tv",
             "Bursaspor Tv",
             "Ntvspor",
             "Ligtv"
             ])
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.browser)
        self.setLayout(layout)
        self.combo.currentIndexChanged.connect(self.get_data)
        self.setWindowTitle("Tv Kanalları Yayın Akışı - beta versiyonu".decode('utf-8'))
        self.resize(400, 650)
        self.browser.clear()
        about = "\nBu program @ozcaan11 tarafından \n" \
                "\n28 Ocak 2016 Perşembe 06:30'da yapılmıştır.\n" \
                "\nBeta versiyonunu kullanmaktasınız."
        self.browser.append(about.decode('utf-8'))

    def get_data(self):
        d = ["saat", "program"]

        def secim(soup):

            for i in soup.findAll("div", {"class": "row current"}):
                saat_current = i.contents[1].string
                prog_current = i.contents[3].string
                d[0] = saat_current
                d[1] = prog_current

            self.browser.clear()
            for i in soup.findAll("div", {"class": re.compile(r'row.*')}):
                try:
                    if not (i.contents[1].string is None or i.contents[3].string is None):
                        if i.contents[1].string is None or i.contents[3].string is None:
                            pass
                        else:
                            if i.contents[1].string == d[0] and i.contents[3].string == d[1]:
                                saat = str(i.contents[1].string).decode('utf-8')
                                program = str(i.contents[3].string).decode('utf-8') + "\n"
                                self.browser.append("=> " + saat + " - " + program.replace('&#39;', "'"))
                            else:
                                saat = str(i.contents[1].string).decode('utf-8')
                                program = str(i.contents[3].string).decode('utf-8') + "\n"
                                self.browser.append("    " + saat + " - " + program.replace('&#39;', "'"))

                                # çektiğimiz site ' karakteri &#39; olarak gösteriliyordu onun için
                                # replace metodunu kullandık

                except:
                    pass

        def no_connection():
            self.browser.clear()
            self.browser.append("İnternet bağlantınızı kontrol edin.".decode('utf-8'))

        if self.combo.currentIndex() == 0:
            self.browser.clear()
            about = "\nBu program @ozcaan11 tarafından \n" \
                    "\n28 Ocak 2016 Perşembe 06:30'da yapılmıştır.\n" \
                    "\nBeta versiyonunu kullanmaktasınız."
            self.browser.append(about.decode('utf-8'))

        if self.combo.currentIndex() == 1:
            try:
                kanal = "http://www.tvyayinakisi.com/kanal-d-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 2:
            try:
                kanal = "http://www.tvyayinakisi.com/fox"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 3:
            try:
                kanal = "http://www.tvyayinakisi.com/show-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 4:
            try:
                kanal = "http://www.tvyayinakisi.com/star-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 5:
            try:
                kanal = "http://www.tvyayinakisi.com/atv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 6:
            try:
                kanal = "http://www.tvyayinakisi.com/trt-1"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 7:
            try:
                kanal = "http://www.tvyayinakisi.com/tv-8"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 8:
            try:
                kanal = "http://www.tvyayinakisi.com/kanal-7"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 9:
            try:
                kanal = "http://www.tvyayinakisi.com/a-haber"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 10:
            try:
                kanal = "http://www.tvyayinakisi.com/cnn-turk"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 11:
            try:
                kanal = "http://www.tvyayinakisi.com/cnbce"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 12:
            try:
                kanal = "http://www.tvyayinakisi.com/kanalturk"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 13:
            try:
                kanal = "http://www.tvyayinakisi.com/samanyolu-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 14:
            try:
                kanal = "http://www.tvyayinakisi.com/ntv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 15:
            try:
                kanal = "http://www.tvyayinakisi.com/tnt"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 16:
            try:
                kanal = "http://www.tvyayinakisi.com/halk-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 17:
            try:
                kanal = "http://www.tvyayinakisi.com/gs-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 18:
            try:
                kanal = "http://www.tvyayinakisi.com/fb-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 19:
            try:
                kanal = "http://www.tvyayinakisi.com/bjk-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 20:
            try:
                kanal = "http://www.tvyayinakisi.com/bursaspor-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 21:
            try:
                kanal = "http://www.tvyayinakisi.com/ntvspor"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()

        if self.combo.currentIndex() == 22:
            try:
                kanal = "http://www.tvyayinakisi.com/lig-tv"
                soup = BeautifulSoup(urllib.urlopen(kanal))
                secim(soup)
            except:
                no_connection()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

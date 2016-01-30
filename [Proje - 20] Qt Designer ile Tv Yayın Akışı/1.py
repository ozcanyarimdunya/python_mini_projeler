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
             "Kanal 7"])
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
                                self.browser.append("=> " + saat + " - " + program)
                            else:
                                saat = str(i.contents[1].string).decode('utf-8')
                                program = str(i.contents[3].string).decode('utf-8') + "\n"
                                self.browser.append("    " + saat + " - " + program)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

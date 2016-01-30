# coding=utf-8

"""
        Tv kanalları yayın akışı
        Öncelikle BeautifulSoup modülünü kurmanız gerekecektir(3 sürümü)
        'sudo pip install beautifulsoup' yazmanız işi halledecektir
        Tam donanımlı :)
"""

import urllib
from BeautifulSoup import *
import time

Kanal_d = "http://www.tvyayinakisi.com/kanal-d-tv"
Fox = "http://www.tvyayinakisi.com/fox"
Show = "http://www.tvyayinakisi.com/show-tv"
Star = "http://www.tvyayinakisi.com/star-tv"
Atv = "http://www.tvyayinakisi.com/atv"
Trt_1 = "http://www.tvyayinakisi.com/trt-1"
Tv8 = "http://www.tvyayinakisi.com/tv-8"
Kanal_7 = "http://www.tvyayinakisi.com/kanal-7"


def kanal(soup, kanal_adi):
    print "Yükleniyor... Lütfen bekleyiniz.\n"
    time.sleep(3)
    print "{}' de bugün".format(kanal_adi)

    for i in soup.findAll("div", {"class": re.compile(r'row.*')}):
        try:
            if not i.contents[1].string is None:
                print i.contents[1].string
        except:
            pass
        try:
            if not i.contents[3].string is None:
                print i.contents[3].string
                print ""
        except:
            pass
    time.sleep(5)
    s = input("\nDiğer kanalları da görmek istiyor musunuz?(Evet: 1, Hayır: -1)")
    if s == 1:
        main()
    else:
        print "Güle güle :)"
        time.sleep(2)


def main():
    print"""
        1 - Kanal D
        2 - Fox Tv
        3 - Show Tv
        4 - Star
        5 - Atv
        6 - Trt 1
        7 - Tv8
        8 - Kanal 7
    """
    time.sleep(1)

    secim = input("\nkanal seçiniz: ")

    if secim == 1:
        soup_kanald = BeautifulSoup(urllib.urlopen(Kanal_d))
        kanal(soup_kanald, "Kanal D")
    elif secim == 2:
        soup_fox = BeautifulSoup(urllib.urlopen(Fox).read())
        kanal(soup_fox, "Fox Tv")
    elif secim == 3:
        soup_show = BeautifulSoup(urllib.urlopen(Show).read())
        kanal(soup_show, "Show Tv")
    elif secim == 4:
        soup_star = BeautifulSoup(urllib.urlopen(Star).read())
        kanal(soup_star, "Star Tv")
    elif secim == 5:
        soup_atv = BeautifulSoup(urllib.urlopen(Atv).read())
        kanal(soup_atv, "Atv")
    elif secim == 6:
        soup_trt1 = BeautifulSoup(urllib.urlopen(Trt_1).read())
        kanal(soup_trt1, "Trt 1")
    elif secim == 7:
        soup_tv8 = BeautifulSoup(urllib.urlopen(Tv8).read())
        kanal(soup_tv8, "Tv8")
    elif secim == 8:
        soup_kanal7 = BeautifulSoup(urllib.urlopen(Kanal_7).read())
        kanal(soup_kanal7, "Kanal 7")
    else:
        print "kanal seçmediniz :("
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()

# @ozcaan11

# coding=utf-8

"""
    Geometrik şekillerin alanlarını hesaplama
"""


def kare(k):
    print "Karenin alanı = {}".format(k * k)


def dikdortgen(u_k, k_k):
    print "Dikdörtgenin alanı = {}".format(k_k * u_k)


def yamuk(a_t, u_t, y):
    print "Yamuğun alanı = {}".format(((a_t + u_t) * y) / 2)


def paralelkenar(k, y):
    print "Paralel kenarın alanı = {}".format(k * y)


def eskenardortgen(a_k, y_k):
    print "Eşkenar dörtgenin alanı = {}".format((a_k * y_k) / 2)


if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    3 - Yamuk
    4 - Paralelkenar
    5 - Eşkenar Dörtgen
    """)

    secim = input("Alanını hesaplamak istediğiniz şekil: ")

    if secim == 1:
        k = input("Karenin bir kenarı: ")
        kare(k)

    if secim == 2:
        k = input("Dikdörtgenin kısa kenarı: ")
        u = input("Dikdörtgenin uzun kenarı: ")
        dikdortgen(k, u)

    if secim == 3:
        a = input("Yamuğun alt taban uzunuğu: ")
        u = input("Yamuğun üst taban uzunuğu: ")
        y = input("Yamuğun yüksekliği: ")
        yamuk(a, u, y)

    if secim == 4:
        k = input("Paralel kenarın alt taban uzunluğu: ")
        y = input("Paralel kenarın yüksekliği: ")
        paralelkenar(k, y)

    if secim == 5:
        a = input("Eşkenar dörtgenin alt kenar uzunluğu: ")
        y = input("Eşkenar dörtgenin yan kenar uzunluğu: ")
        eskenardortgen(a, y)

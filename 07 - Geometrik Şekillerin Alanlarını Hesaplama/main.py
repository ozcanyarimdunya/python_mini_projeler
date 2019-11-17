# coding=utf-8

"""
    Geometrik şekillerin alanlarını hesaplama
"""


def kare(k):
    print("Karenin alanı = {}".format(k * k))


def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))


def yamuk(a_t, u_t, y):
    print("Yamuğun alanı = {}".format(((a_t + u_t) * y) / 2))


def paralelkenar(k, y):
    print("Paralel kenarın alanı = {}".format(k * y))


def eskenardortgen(a_k, y_k):
    print("Eşkenar dörtgenin alanı = {}".format((a_k * y_k) / 2))


if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    3 - Yamuk
    4 - Paralelkenar
    5 - Eşkenar Dörtgen
    """)

    secim = int(input("Alanını hesaplamak istediğiniz şekil: "))

    if secim == 1:
        k = int(input("Karenin bir kenarı: "))
        kare(k)

    elif secim == 2:
        k = int(input("Dikdörtgenin kısa kenarı: "))
        u = int(input("Dikdörtgenin uzun kenarı: "))
        dikdortgen(k, u)

    elif secim == 3:
        a = int(input("Yamuğun alt taban uzunuğu: "))
        u = int(input("Yamuğun üst taban uzunuğu: "))
        y = int(input("Yamuğun yüksekliği: "))
        yamuk(a, u, y)

    elif secim == 4:
        k = int(input("Paralel kenarın alt taban uzunluğu: "))
        y = int(input("Paralel kenarın yüksekliği: "))
        paralelkenar(k, y)

    elif secim == 5:
        a = int(input("Eşkenar dörtgenin alt kenar uzunluğu: "))
        y = int(input("Eşkenar dörtgenin yan kenar uzunluğu: "))
        eskenardortgen(a, y)

    else:
        print("Sadece belirtilen sayılardan birini giriniz.")

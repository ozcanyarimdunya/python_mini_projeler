# coding=utf-8

"""
    Geometrik şekillerin alanlarını hesaplama
"""


def kare(k):
    """
    Kare kare kares

    Args:
        k: (todo): write your description
    """
    print("Karenin alanı = {}".format(k * k))


def dikdortgen(k, u):
    """
    Dikdortdortgen.

    Args:
        k: (todo): write your description
        u: (todo): write your description
    """
    print("Dikdörtgenin alanı = {}".format(k * u))


def yamuk(a_t, u_t, y):
    """
    Yamuk of yampling

    Args:
        a_t: (todo): write your description
        u_t: (todo): write your description
        y: (todo): write your description
    """
    print("Yamuğun alanı = {}".format(((a_t + u_t) * y) / 2))


def paralelkenar(k, y):
    """
    Paralelelken test of k

    Args:
        k: (todo): write your description
        y: (todo): write your description
    """
    print("Paralel kenarın alanı = {}".format(k * y))


def eskenardortgen(a_k, y_k):
    """
    Generate k_kortgenortortgenardardort

    Args:
        a_k: (todo): write your description
        y_k: (todo): write your description
    """
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

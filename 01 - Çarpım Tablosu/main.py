#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

"""
    Küçük çapta bir çarpım tablosu uygulaması
"""

print("-" * 50)
print("\t\tHOŞGELDİNİZ..")
print("-" * 50, "\n")


def carpim(i, j, r):
    if r != "-1":
        result = str(i * j)
        if result == r:
            print("\t\t***** Doğru *****")
        else:
            print("\t!!! Yanlış cevap %s olacaktı" % result)
    else:

        secim()


def basla(rng_1, rng_2):
    if rng_1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            sayi_1 = randint(rng_1, rng_2)
            sayi_2 = randint(rng_1, rng_2)
            print("_" * 50, "\n")
            print("\t%d x %d kaça eşittir? (çıkış = -1)" % (sayi_1, sayi_2))
            sonuc = input("sonuc >> ")
            carpim(sayi_1, sayi_2, sonuc)

            if i == 4 and j == 4:
                print("\n *-- Bu bölüm bitti bir üst bölüme geçebilsiniz --*\n")
                secim()


def secim():
    print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = -1) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    svy = input(" >> ")

    if svy == "1":
        basla(1, 6)

    elif svy == "2":
        basla(6, 12)

    elif svy == "3":
        basla(12, 25)

    elif svy == "4":
        basla(25, 100)

    else:
        exit(0)


if __name__ == '__main__':
    secim()

# @ozcanyarimdunya

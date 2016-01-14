# coding=utf-8

"""
    Küçük çapta bir çarpım tablosu uygulaması
"""

print "-"*50, "\n"

def carpim(i, j, r):
    if r != -1:
        if i*j == r:
            print "***** Doğru *****"
        else:
            print "!!! Yanlış cevap %s olacaktı"%(i*j)
    else:
        exit(0)

def basla(rng_1, rng_2):
    for sayi_1 in range(rng_1, rng_2):
        for sayi_2 in range(rng_1-1, rng_2):
            print "_"*50, "\n"
            print "\t%d x %d kaça eşittir? (çıkış = -1)"%(sayi_1, sayi_2)
            sonuc = input("sonuc >> ")
            carpim(sayi_1, sayi_2, sonuc)


if __name__ == '__main__':
    print "Hangi seviyeden başlamak istiyorsunuz ?"
    print "  1 - Kolay "
    print "  2 - Orta "
    print "  3 - Zor"
    print "  4 - Çok zor"
    svy = input(" >> ")
    if svy == 1:
        basla(1, 6)
    if svy == 2:
        basla(6, 11)
    if svy == 3:
        basla(11, 21)
    if svy == 4:
        basla(22, 100)

# @ozcaan11
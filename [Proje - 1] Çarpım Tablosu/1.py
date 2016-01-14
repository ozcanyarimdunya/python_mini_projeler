# coding=utf-8

"""
    Küçük çapta bir çarpım tablosu uygulaması
"""

print "-"*50, "\n"
print " "*20, "HOSGELDINIZ", "\n"
print "-"*50, "\n"

def carpim(i, j, r):
    if r != -1:
        if i*j == r:
            return "***** Doğru *****"
        else:
            return "!!! Yanlış cevap %s olacaktı"%(i*j)
    else:
        exit(0)


def baslangic():
    for sayi_1 in range(1, 6):
        for sayi_2 in range(0, 6):
            print "_"*50, "\n"
            print "\t%d x %d kaça eşittir(çıkış = -1)"%(sayi_1, sayi_2)
            sonuc = input("sonuc = ")
            print carpim(sayi_1, sayi_2, sonuc)


if __name__ == '__main__':
    baslangic()
# coding=utf-8

"""
    Faktoriyel alma programı
"""

def fact(sayi):
    if sayi == 0:
        return 1

    elif sayi == 1:
        return 1
    else:
        return sayi*fact(sayi-1)
if __name__ == '__main__':
    print fact(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))
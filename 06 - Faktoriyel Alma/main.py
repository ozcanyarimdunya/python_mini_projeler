# coding=utf-8

"""
    Faktoriyel alma programı
"""


def fact(sayi):
    """
    R returns the fact of a fact.

    Args:
        sayi: (array): write your description
    """
    if sayi <= 1:
        return 1
    else:
        return sayi * fact(sayi - 1)


if __name__ == '__main__':
    sayi = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))

    print(fact(sayi))

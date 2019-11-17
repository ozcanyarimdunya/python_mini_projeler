# coding=utf-8

"""
    Bulunduğumuz dizinde;

        1 - Yeni bir klasör oluşturma
        2 - Dizindeki klasörleri listeleme
        3 - Dizindeki klasörleri silme
"""

import os


def yeni_klasor():
    dosya = input("Oluşturacağınız klasörün adı: ")

    if os.path.exists(dosya):
        print("{} adında bir klasör zaten var. Başka bir isim seçin. ".format(dosya))
    else:
        os.makedirs(dosya)


def dizini_listele():
    print("{}/\n...".format(os.getcwd()))

    for a, i in enumerate(os.listdir(os.curdir)):
        print("{}  {}".format(a, i))


def klasor_silme():
    dizin = {}
    print("\nno\t\tdosya adı\n--\t\t---------")

    for a, i in enumerate(os.listdir(os.curdir)):
        print("{}\t\t{}".format(a, i))
        dizin[a] = i

    try:
        d_no = int(input("Silmek istediğiniz dosya numarası: "))
        path = dizin[d_no]
        os.removedirs(path)

    except KeyError:
        print("KeyError:Klasör silinemedi !")
    except NameError:
        print("NameError:Klasör silinemedi !")
    except SyntaxError:
        print("SyntaxError:Klasör silinemedi !")


def main():
    print("""
    'os' modülü ile dosya işlemleri
    -----------------------------

    1 - Yeni klasör oluşturma
    2 - Dizindeki klasörleri listeleme
    3 - Klasör silme

    """)
    try:
        secim_no = int(input("Yapmak istediğiniz işlem numarası: "))

        while True:
            if secim_no == 1:
                yeni_klasor()
                break

            if secim_no == 2:
                dizini_listele()
                break

            if secim_no == 3:
                klasor_silme()
                break

            else:
                print("İşlem seçilmedi !")
                break

    except KeyError:
        print("İşlem seçilmedi !")
    except NameError:
        print("İşlem seçilmedi !")
    except SyntaxError:
        print("İşlem seçilmedi !")


if __name__ == '__main__':
    main()

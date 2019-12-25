# coding=utf-8

"""
    Öğrenci ekle/sil/ara/listele

    Öncelikle pymongo modülünü kurmanız gerekiyor
    Bunun için " sudo pip install pymongo " diye yazın terminale gerisi halleder zaten.
    db_ogrenciler adında bir database miz var
    ogrenci adında bir collectionumuz var.
    Table dememin sebebi SQL de table diye geçiyor ondan
"""
from pymongo import MongoClient

db = MongoClient(host='localhost', port=27017)['db_ogrenciler']
table = db['ogrenci']


def ogr_ekle():
    no = int(input("öğrenci no: "))
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyadı: ")

    table.insert({"no": int(no), "ad": ad, "soyad": soyad})
    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri eklendi ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))


def ogr_sil():
    no = int(input("silmek istediğiniz öğrencinin numarasını giriniz: "))

    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri silindi ---
               numara  : {}
               ad      : {}
               soyad   : {}""".format(i['no'], i['ad'], i['soyad']))

    table.delete_one({"no": no})


def ogr_ara():
    no = int(input("aramak istediğiniz öğrencinin numarasını giriniz: "))

    table.find({"no": no})
    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri bulundu ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))


def ogr_lis():
    sonuc = table.find()
    for (a, i) in enumerate(sonuc):
        print(
            """
                   --- {} ---
                   numara  : {}
                   ad      : {}
                   soyad   : {} """.format(a, i['no'], i['ad'], i['soyad']))


def main():
    print(
        """
           Öğrenci Kayıt Otomasyonu
       
           1 - Öğrenci ekle
           2 - Öğrenci ara
           3 - Öğrenci sil
           4 - Öğrenci listesi
           """)
    secim = int(input("Yapmak istediğiniz işlem: "))
    while True:
        if secim == 1:
            ogr_ekle()
            break
        if secim == 2:
            ogr_ara()
            break
        if secim == 3:
            ogr_sil()
            break
        if secim == 4:
            ogr_lis()
            break


if __name__ == '__main__':
    main()

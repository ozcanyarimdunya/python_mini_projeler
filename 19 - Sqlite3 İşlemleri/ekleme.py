# coding=utf-8

from baglanti import islem

# TABLOYA VERİ EKLEME
# tablomuza veri ekleme kısmı en kolayı parantez içinde ad.soyad kısımlarını yazmayadabilirdik
# amaç sırasıyla neyi kaydediyoruz onu anlamak
# çift veya tek tırnak olayını dikkatli bir şekilde yapın
# bu kodda kullanıcıdan bir istek almadan direkt kaydettik
islem.execute("INSERT INTO ogrenci (ad, soyad, bolum, sinif) VALUES ('ozcan','yrmdny','bilg. muh.',4)")

# kullanıcı etkileşimli insert işlemleri için şöyle yapmalıyız
ogr_ad = "ali"  # buraya raw_input("öğrenci adı: ") da diyebiliriz
ogr_soyad = "veli"  # raw_input("öğrenci soyadı: ")
ogr_bolum = "endustri"  # raw_input("öğrenci bölüm: ")
ogr_sinif = 4  # int(raw_input("öğrenci bölümü: ")) integera çevirmek şart
# çünkü bu kolon veri tabanında int olarak tanımlanmış

# bu işlem kullanıcı tarafından girilen değerleri veritabanına kaydedecektir
# ya da bir değişkene atanıp gönderilen değeri
islem.execute('''INSERT INTO ogrenci VALUES (?,?,?,?)''', (ogr_ad, ogr_soyad, ogr_bolum, ogr_sinif))

islem.execute("select * from ogrenci")
for i in islem.fetchall():
    print(i)

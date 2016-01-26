# coding=utf-8

"""
    sqlite3 veritabanı işlemleri
    okul adında veritabanına
    ogrenci adında bir tablo ekleyelim
    ogrenci tablosu öğrenci bilgilerini tutsun(ad,soyad,bölüm,sınıf)
"""

import sqlite3

# BAĞLANMA
# okul.db adında yeni bir veri tabanı oluşturduk
# baglanmak için
baglan = sqlite3.connect("okul.db")

# baglandığımız veri tabanı üzerinde işlemler yapmak için
# cursor fonksiyonunu kullanıyoruz hala da ne işe yaradığını bilmiyorum
islem = baglan.cursor()


# TABLO OLUŞTURMA
# Mutlaka ilk olarak tablomuzu oluşturmalıyız
# if not exist dememizin sebebi her defasında bu kodları çalıştırdığımızda
# yeniden aynı adda tablo oluşturamayacağı için denetleme yapıyoruz
# böyle bir tablo yoksa oluştur varsa zaten hiç dokunma
islem.execute("CREATE TABLE IF NOT EXISTS ogrenci(ad TEXT, soyad TEXT, bolum TEXT, sinif INT)")



# TABLODAKİ VERİLERİ GÜNCELLEME
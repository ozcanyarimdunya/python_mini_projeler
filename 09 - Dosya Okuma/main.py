# coding=utf-8

"""
    Dosya okuma ve yazma işlemleri
    Öğrenci notlarını tutan bir dosya olsun
"""

# Yazmak için dosya oluştur

dosya = open('notlar.text', 'w')

notlar = {
    "ali": 45,
    "ahmet": 90,
    "veli": 75,
    "mehmet": 60,
    "serdar": 85,
    "ayse": 40
}

for item in notlar.items():
    dosya.write(str(item))
    dosya.write('\n')

dosya.close()

# Dosyayı okumak için tekrar açtık
dosya = open('notlar.text', 'r')
for i in dosya.readlines():
    print(i)

dosya.close()

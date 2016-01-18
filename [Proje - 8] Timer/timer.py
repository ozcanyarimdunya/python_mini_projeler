# coding=utf-8
import time

# time.sleep(5)
zaman = time.localtime()

yil = zaman[0]
ay = zaman[1]
gun = zaman[2]
saat = zaman[3]
dakika = zaman[4]
saniye = zaman[5]

while True:
    print("""
    tarih: {}/{}/{}
    saat : {}:{}:{}
    """).format(gun, ay, yil, saat, dakika, saniye)
    break

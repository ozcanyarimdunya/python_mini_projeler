# coding=utf-8
"""
    Eskişehir hava durumu
    İlk defa regular expresiionlarlar çalıştığım için
    biraz abartılı dolambaçlı olmuş olabilir :)
"""

import re
import requests

url = "http://www.havadurumu15gunluk.net/havadurumu/eskisehir-hava-durumu-15-gunluk.html"
site = requests.get(url).content.decode('utf-8')

r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
r_aciklama = '<img src="/havadurumu/images/trans.gif" alt="Eskişehir Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

comp_gunduz = re.compile(r_gunduz)
comp_gece = re.compile(r_gece)
comp_gun = re.compile(r_gun)
comp_tarih = re.compile(r_tarih)
comp_aciklama = re.compile(r_aciklama)

gunduz = []
gece = []
gun = []
tarih = []
aciklama = []

for i in re.findall(r_gunduz, site):
    gunduz.append(i)

for i in re.findall(r_gece, site):
    gece.append(i)

for i in re.findall(r_gun, site):
    gun.append(i)

for i in re.findall(r_tarih, site):
    tarih.append(i)

for i in re.findall(r_aciklama, site):
    aciklama.append(i)

print("-" * 75)
print("                         ESKİŞEHİR HAVA DURUMU")
print("-" * 75)
for i in range(0, len(gun)):
    print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i], aciklama[i]))
    print("-" * 75)

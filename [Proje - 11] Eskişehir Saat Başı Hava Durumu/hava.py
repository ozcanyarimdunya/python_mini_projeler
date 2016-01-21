# coding=utf-8
"""
    Eskişehir saatlik hava durumu
    <th class="nem1" style="color:#4247b8; font-weight:bold; background-color:#ecf4f8; ">94</th>
"""
import re, urllib

url = "http://www.mgm.gov.tr/tahmin/default.aspx?s=ESKISEHIR"
html = urllib.urlopen(url).read()

regex_sicaklik = '<th class="sicak1" style="font-weight:bold; ' \
                 'color:red; background-color:#ecf4f8;">(.*)</th>'

regex_nem = '<th  class="nem1" style="color:#4247b8; ' \
            'font-weight:bold; background-color:#ecf4f8; ">(\d+)</th>'

regex_ruzgar = '<th class="ruzgarham1" style="color:#731d75; ' \
               'font-weight:bold; background-color:#ecf4f8; ">(\d+)</th>'

regex_saat = '<th style="color:#8095a4; background-color:#ecf4f8; ' \
             'font-weight:normal;">([\d+][\d+]:00)</th>'

comp_sicaklik = re.compile(regex_sicaklik)
comp_nem = re.compile(regex_nem)
comp_ruzgar = re.compile(regex_ruzgar)
comp_saat = re.compile(regex_saat)

sicaklik = []
nem = []
ruzgar = []
saat = []

for i in re.findall(comp_sicaklik, html):
    print i
    sicaklik.append(i)

for i in re.findall(comp_nem, html):
    nem.append(i)

for i in re.findall(comp_ruzgar, html):
    ruzgar.append(i)

for i in re.findall(comp_saat, html):
    saat.append(i)


print """
ESKİŞEHİR SAAT BAŞI HAVA DURUMU
-------------------------------
"""
for i in range(0, len(saat)):
    print "saat: {},\tsıcaklık: ?,\tnem: {},\truzgar: {}".format(saat[i], nem[i], ruzgar[i])

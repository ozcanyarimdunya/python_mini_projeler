# coding=utf-8

"""
            Girilen bir yazıyı tersten yazdırma

    # ----- BÜTÜN CÜMLEYİ TERS ÇEVİRME -----
    # Bu yöntem cümleyi tümüyle ters çeviriyor
    # tersini_alma fonksiyonu direkt bu işlemi yapmaktadır

    # ----- KELİME KELİME TERSİNE ÇEVİRME -----
    # Bu yöntem cümleyi kelime kelime ters çeviriyor
    # Öncelikle cümleyi boşluk karakterine göre split(ayırma) yapıp bir diziye atayalım
    # Sonra bu dizinin her elemanını tersine çevirelim
    # Zaten tersini alma fonksiyonu gelen stringi tersine çeviriyordu
    # O yüzden bizde burda her bir stringimizi teker teker o fonksiyona göndereceğiz
    # Tersini aldıktan sonra " ".join ile dizimiz birleşik yazacağız
"""


print "NOT: - Türkçe karakter sorunu maalesef var :( -\n"

girilen_yazi = raw_input("cümle girin: ")
yazinin_tersi = ""



def tersini_alma(yazi, tersi):
    for i in range(len(yazi)-1, -1, -1):
        tersi += yazi[i]
    return tersi


kelimeler = []
for i in girilen_yazi.split(' '):
    kelimeler.append(tersini_alma(i, ""))


cumle_halinde_tersi  = tersini_alma(girilen_yazi, yazinin_tersi)
kelime_halinde_tersi = " ".join(kelimeler)

print """
Cümlenin orjinali:                  {}

Tamamen tersi alınmış hali:         {}

Kelime kelime tersi alınmış hali:   {}

""".format(girilen_yazi, cumle_halinde_tersi, kelime_halinde_tersi)














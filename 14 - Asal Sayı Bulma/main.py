# coding=utf-8

"""
    Girdiğimiz bir sayıya kadar ki asal olan bütün sayıları listeleme
"""

deger = int(input("Kaça kadar ki asal sayıları arıyorsunuz? : "))
asal = []

for i in range(2, deger):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        asal.append(i)
        
dosya = open('asalSayi.txt', 'w')
dosya.write(f'0 - {deger} Arasinda Olan Asal Sayilar: ')
dosya.write(str(asal))
#print("\n0 - {} arasında toplam {} tane asal sayı vardır.".format(deger, len(asal)))

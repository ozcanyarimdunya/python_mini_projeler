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

print("\n0 - {} arasında toplam {} tane asal sayı vardır.".format(deger, len(asal)))

# coding=utf-8

"""
    Girdiğimiz bir sayıya kadar ki asal olan bütün sayıları listeleme
"""

deger = int(input("Kaça kadar ki asal sayıları arıyorsunuz? : "))
asal = []

for i in range(2, deger):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        asal.append(i)

for i in asal:
    print(i)

print("\n0 - {} arasında toplam {} tane asal sayı vardır.".format(deger, len(asal)))

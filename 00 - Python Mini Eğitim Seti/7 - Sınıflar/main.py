# coding=utf-8
from __future__ import print_function

"""
    Sınıflar sürekli tekrar eden kodları fonksiyonları daha az kod yazarak
    kullanmamızı sağlıyor.

"""

# Önce class adını tanımlayacağız
class MyClass:
    """
        Burası MyClass.__doc__() yazıldığında görüntülenecek yer
        __init__ içine tanımlayacağımız değerler sınıfın için alacağı  değerleri gösterir
    """
    def __init__(self,name,number):
        """
            sınıf tanımlanırken  sınıfın içine name ve number değişkenleri alacak
        """
        # self.name diye bir değişken tanımlayıp gelen name değişkenini
        # bu name değişkenine atıyoruz
        # bu sayede gelen değişkeni altta yazacağımız her fonksiyonda kullanbileceğiz
        self.name = name

        self.number = number

        """
            Burada özel bir değişken tanımladık
            Bu değişkenin özel olabilmesi için başında iki tane __ olmalı
            Bu değişkene direkt erişemiyoruz ancak bir fonksiyon yardımı olmalı
        """
        self.__privateValue = "private value"

    def printing(self):
        print("""
        printing function
            name  : {}
            number: {}
            {}
        """.format(self.name,self.number,self.__privateValue))

    def makePrivateAccessible(self,publicValue):
        self.__privateValue = publicValue

    def OutSideFunc(self):
        """
            Bu fonksiyonla bu classtan yeni bi nesne tanımladığında kodu azaltmak için
            erişim sağlayacağımız fonksiyondur
        """
        print("Outside Function")

"""
    Sınıfımızdan yeni bir nesne türetiyoruz
"""

nesne = MyClass(name="my name",number=12)
nesne.printing()
nesne.makePrivateAccessible("public value")
nesne.printing()
nesne.OutSideFunc()


"""
        OUTPUT


        printing function
            name  : my name
            number: 12
            private value


        printing function
            name  : my name
            number: 12
            public value

    Outside Function

"""
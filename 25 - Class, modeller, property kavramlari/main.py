"""
Her dilde oldugu gibi python da da model tanimlarmalari yapip onlari daha etkili kullanabilirsiniz
Orn: User sinifiniz olsun bunun property leri olsun (id, name, age) gibi
Bunlara init degilde  herhangi bir yerde deger verme islemleri icin modelleme yapilarini kullaniriz
"""


class User:

    def __init__(self, name=None, age=None):
        """
        Initialize a new instance.

        Args:
            self: (todo): write your description
            name: (str): write your description
            age: (str): write your description
        """
        self.__name = name  # __(iki alttan tire) ile basladiysa bu private oldugu anlamina gelir
        self.__age = age  # herhangi bir yerden buna ulasilamaz taa ki getter ve setter property leri yapilincaya kadar

    def __str__(self):
        """
        Return the string representation of the object.

        Args:
            self: (todo): write your description
        """
        return "<< User: name={}, age={} >>".format(self.name, self.age)

    @property
    def name(self):
        """
        The name of the name

        Args:
            self: (todo): write your description
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Sets the name.

        Args:
            self: (todo): write your description
            value: (str): write your description
        """
        self.__name = value

    @property
    def age(self):
        """
        Return the age.

        Args:
            self: (todo): write your description
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Set the age.

        Args:
            self: (todo): write your description
            value: (todo): write your description
        """
        self.__age = value


if __name__ == '__main__':
    user = User(name="Ozcan", age=24)
    print(user)  # OUTPUT: << User: name=Ozcan, age=24 >>

    user.name = "Abc"  # setter
    print(user)  # OUTPUT: << User: name=Abc, age=24 >>

    print(user.name, user.age)  # OUTPUT:  Abc 24

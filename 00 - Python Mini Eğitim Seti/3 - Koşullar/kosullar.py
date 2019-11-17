# coding=utf-8

"""
    Koşullar deyince aklımıza direkt isminden de anlaşılacağı gibi
    şartlı yapılar gelsin
    Kısaca eğer bu şart sağlanıyorsa, şunu yap
    Örneğin eğer x, 5'e eşitse, x, 5'e eşittir yazdır ekrana
    Tabi programlama dillerini ingilizce olarak yazdığımız için (ne yazık ki!)
    Mecbur ingilizce kalıplar kullanacağız
    Örneğin if x equal to 5, print x equal to 5
    Örnekte daha anlaşılır olacaktır.
"""

x = 5  # x sayısını başta 5'e eşitledik

if x == 5:  # eğer x, 5'e eşitse (!!!) burada eşittir koşulu
    print("x, 5'e eşittir!")  # == işareti ile ve koşul sonrasında : kullanılması mecburidir
elif x == 4:  # elif = else if yani ya da eğer x, 4'e eşitse
    print("x, 5'e eşit değildir. x = ", x)
elif x != 5:  # x, 5'e eşit değilse anlamında geliyor != işareti
    print("x, 5'e eşit değildir!")
else:  # else dan sonra bir koşul belirtilmez!!!!
    print("x nedir ya?")

"""
Output:

x, 5'e eşittir!

Process finished with exit code 0
"""

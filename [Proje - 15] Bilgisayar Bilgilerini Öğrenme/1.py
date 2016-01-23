# coding=utf-8

"""
    Bilgisayar bilgilerini öğrenme
    Bu benim bilgisayarım için doğru bir şekilde çalıştı.
    Ama sizin bilgisayarınızda farklılık gösterebilir veya çalışmayadabilir.
    Eğer Ubuntu kullanıyorsanız %75 doğru çalışacaktır.

"""

import os

b = os.uname()
print """
    İşletim sistemi : {} {}
    Bilgisayar adı  : {}
    Model           : {}
    Sürüm           : {}
    Sürüm tarihi    : {}
""".format(
    b[0], b[4],
    b[1],
    b[3].split('~')[1].split(' ')[0],
    b[2],
    b[3].split('-')[1]
)


"""
    Uygulamayı çalıştırdığınızda böyle bir sonuç elde etmeniz lazım


    İşletim sistemi : Linux x86_64
    Bilgisayar adı  : MY-LINUX
    Model           : 14.04.1-Ubuntu
    Sürüm           : 3.19.0-47-generic
    Sürüm tarihi    : Ubuntu SMP Mon Jan 18 16:09:14 UTC 2016

"""
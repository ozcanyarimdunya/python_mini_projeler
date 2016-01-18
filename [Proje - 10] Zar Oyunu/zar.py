# coding=utf-8

import random
import time

"""
    2 adet zar atılsın ve her iki zarın değeri de 6 olduğunda program dursun.
    İki zar da 6 gelene kadar kaç kez zar atıldığını bildiren programı yazınız.
"""


i = 1
while True:
    zar_1 = random.randint(1, 6)
    zar_2 = random.randint(1, 6)

    if zar_1 == 6 and zar_2 == 6:
        print """Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2)
        time.sleep(2)
        break

    print """Deneme {}:\t({},{}) """.format(i, zar_1, zar_2)
    i += 1
    time.sleep(0.5)

print """\n*** {}. denemede (6,6) geldi ***""".format(i)


# @ozcaan11
# coding=utf-8

"""
 n: disk sayısı,
 s: kaynak,
 t: hedef,
 b: tampon

"""


def hanoi(n, s, t, b):
    assert n > 0
    if n == 1:
        print('move', s, 'to', t)
    else:
        hanoi(n - 1, s, b, t)
        hanoi(1, s, t, b)
        hanoi(n - 1, b, t, s)


if __name__ == '__main__':
    hanoi(7, 1, 2, 1)

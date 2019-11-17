# coding=utf-8

"""
    Sözlük içinde anahtar ve değer bulunduran bir nevi dizilerdir
"""

sozluk = {"anahtar_1": "değer_1", "anahtar_2": 3, "abc": "özcan"}

print(sozluk["anahtar_1"])  # değer_1
print(sozluk.keys())  # ['abc', 'anahtar_2', 'anahtar_1']
print(sozluk.values())  # ['özcan', 3, 'değer_1']

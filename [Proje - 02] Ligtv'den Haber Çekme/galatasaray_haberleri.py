# coding=utf-8

import feedparser

"""
    ligtv haberleri feed ile ayrıştırma
    Öncelikle feedparser modülünü indirip kurmanız gerekli
    Terminalde  pip install feedparser  yapıp çalıştırsanız yeterli olacaktır
"""

print('''
    ######################################
    #                                    #
    #    Ligtv Galatasaray Haberleri     #
    #                                    #
    ######################################
''')
haberler_galatasaray = feedparser.parse('http://www.ligtv.com.tr/rss/takim/galatasaray')

i = 1
for haber in haberler_galatasaray.entries:
    print(i, haber.title)
    print("  ", haber.guid, "\n")
    i += 1

# -*- coding: utf-8 -*-

from __future__ import print_function

import os
from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import *

import scrapper

# region Init
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# endregion

"""
    This is for QListWidgetItem Click Events
"""


class MyList(QListWidget):
    def addItemToList(self):
        """
            Buraya scrapperdan gelecek veriler eklenecek
        """
        channels = scrapper.AllChannels()
        channels.downloadIcons()

        for c, channel in enumerate(channels.getChannels()):
            item = QListWidgetItem(channel["name" + str(c)])
            item.setIcon(QIcon(r"icons" + os.sep + str(channel["link" + str(c)])))
            self.addItem(item)
        self.itemClicked.connect(self.item_click)

    def item_click(self, item):
        print(str(item.text()))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(550, 530)

        """
            This is a custom ListWidget :)
        """
        self.lwChannels = MyList(Form)
        self.lwChannels.setGeometry(QtCore.QRect(10, 10, 221, 511))
        self.lwChannels.setObjectName(_fromUtf8("lwChannels"))
        self.lwBroadcasts = QtGui.QListWidget(Form)
        self.lwBroadcasts.setGeometry(QtCore.QRect(240, 10, 301, 461))
        self.lwBroadcasts.setObjectName(_fromUtf8("lwBroadcasts"))
        self.btnYenile = QtGui.QPushButton(Form)
        self.btnYenile.setGeometry(QtCore.QRect(240, 480, 301, 41))
        self.btnYenile.setObjectName(_fromUtf8("btnYenile"))

        self.lwChannels.addItemToList()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnYenile.setText(_translate("Form", "Yenile", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

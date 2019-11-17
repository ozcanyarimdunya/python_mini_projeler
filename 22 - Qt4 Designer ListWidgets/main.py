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


class Ui_Form(object):
    def __init__(self):
        self.link = ""

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(650, 650)

        self.lwChannels = QtGui.QListWidget(Form)
        self.lwChannels.setGeometry(QtCore.QRect(10, 10, 250, 630))
        self.lwChannels.setObjectName(_fromUtf8("lwChannels"))

        self.lwBroadcast = QtGui.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lwBroadcast.setFont(font)
        self.lwBroadcast.setGeometry(QtCore.QRect(270, 70, 370, 570))
        self.lwBroadcast.setObjectName(_fromUtf8("lwBroadcast"))

        self.lblBroadcasting = QtGui.QLabel(Form)
        self.lblBroadcasting.setGeometry(QtCore.QRect(300, 15, 370, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblBroadcasting.setFont(font)
        self.lblBroadcasting.setWordWrap(True)
        self.lblBroadcasting.setObjectName(_fromUtf8("lblBroadcasting"))

        self.addItemList()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addItemList(self):
        channels = scrapper.AllChannels()
        channels.downloadIcons()

        for c, channel in enumerate(channels.getChannels()):
            item = QListWidgetItem(channel["name" + str(c)])
            item.setIcon(QIcon(r"icons" + os.sep + str(channel["link" + str(c)])))
            self.lwChannels.addItem(item)
        self.lwChannels.itemClicked.connect(self.item_click)

    def item_click(self, item):
        self.lwBroadcast.clear()
        channels = scrapper.AllChannels()
        for c, channel in enumerate(channels.getChannels()):
            itm = QListWidgetItem(channel["name" + str(c)])
            if item.text() == itm.text():
                self.link = str(channel["link" + str(c)])
                self.lblBroadcasting.setText(channel["title" + str(c)])

        single_channel = scrapper.SingleChannels(self.link)
        for i in single_channel.getBroadcasting():
            item = QListWidgetItem(i)
            self.lwBroadcast.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

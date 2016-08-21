# -*- coding: utf-8 -*-

"""
    Proje - 1 de yaptığım çarpım toblosunun arayüz ile yapılmış hali
    Qt4 Designer ile dizaynı tamamladıktan sonra dosyayı kaydedin (örn. design.ui)
    Terminal ekranında ' pyui4 -x design.ui -o main.py ' yazdığınızda yaptığınız dizaynı
     sizin için python kodlarına çevirecektir . Gerisi algoritma artık

"""

from PyQt4 import QtCore, QtGui
from random import randint

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


class Ui_mainForm(object):
    def __init__(self):
        self.levelValue = [1, 6]

    def setupUi(self, mainForm):
        mainForm.setObjectName(_fromUtf8("mainForm"))
        mainForm.setWindowModality(QtCore.Qt.NonModal)
        mainForm.resize(425, 277)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainForm.sizePolicy().hasHeightForWidth())
        mainForm.setSizePolicy(sizePolicy)
        mainForm.setMaximumSize(QtCore.QSize(425, 385))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        mainForm.setFont(font)
        self.horizontalLayoutWidget = QtGui.QWidget(mainForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 411, 91))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_firstNo = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_firstNo.setFont(font)
        self.lbl_firstNo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_firstNo.setObjectName(_fromUtf8("lbl_firstNo"))
        self.horizontalLayout.addWidget(self.lbl_firstNo)
        self.lblX = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.lblX.setFont(font)
        self.lblX.setAlignment(QtCore.Qt.AlignCenter)
        self.lblX.setObjectName(_fromUtf8("lblX"))
        self.horizontalLayout.addWidget(self.lblX)
        self.lbl_secondNo = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lbl_secondNo.setFont(font)
        self.lbl_secondNo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_secondNo.setObjectName(_fromUtf8("lbl_secondNo"))
        self.horizontalLayout.addWidget(self.lbl_secondNo)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(mainForm)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 160, 411, 80))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.txtSonuc = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.txtSonuc.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.txtSonuc.setObjectName(_fromUtf8("txtSonuc"))
        self.horizontalLayout_3.addWidget(self.txtSonuc)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(mainForm)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 210, 411, 71))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lblStatus = QtGui.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblStatus.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.lblStatus)
        self.lblSonuc = QtGui.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblSonuc.setFont(font)
        self.lblSonuc.setStyleSheet('color: black')
        self.lblSonuc.setObjectName(_fromUtf8("lblSonuc"))
        self.horizontalLayout_4.addWidget(self.lblSonuc)
        self.comboBox = QtGui.QComboBox(mainForm)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 411, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 21))
        self.label.setObjectName(_fromUtf8("lblBroadcasting"))

        # This is for the clicked methods
        self.clicked()

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(_translate("mainForm", "Çarpım Tablosu", None))
        self.lblX.setText(_translate("mainForm", "X", None))
        self.txtSonuc.setPlaceholderText(_translate("mainForm", " cevabınız ..", None))
        self.comboBox.setItemText(0, _translate("mainForm", "Kolay", None))
        self.comboBox.setItemText(1, _translate("mainForm", "Orta", None))
        self.comboBox.setItemText(2, _translate("mainForm", "Zor", None))
        self.comboBox.setItemText(3, _translate("mainForm", "Çok Zor", None))
        self.label.setText(_translate("mainForm", "Seviye seçin ..", None))

        self.initializeRandoms()

    def initializeRandoms(self):
        self.lbl_firstNo.setText(str(randint(self.levelValue[0], self.levelValue[1])))
        self.lbl_secondNo.setText(str(randint(self.levelValue[0], self.levelValue[1])))
        self.txtSonuc.setText("")
        self.txtSonuc.setFocus()

    def clicked(self):
        self.txtSonuc.returnPressed.connect(self.onEnterClicked)
        self.comboBox.currentIndexChanged.connect(self.onLevelChanged)

    def onEnterClicked(self):
        n1 = int(self.lbl_firstNo.text())
        n2 = int(self.lbl_secondNo.text())
        result = self.txtSonuc.text()

        if str(n1 * n2) == result:
            self.lblStatus.setText("Tebrikler !! ")
            self.lblSonuc.setText("{} x {} = {}".format(str(n1), str(n2), str(n1 * n2)))
            self.lblStatus.setStyleSheet('color: green')
        else:
            self.lblStatus.setText("Yanlış !! ".decode('utf-8'))
            self.lblSonuc.setText("{} x {} = {}".format(str(n1), str(n2), str(n1 * n2)))
            self.lblStatus.setStyleSheet('color: red')

        self.initializeRandoms()

    def onLevelChanged(self):
        if self.comboBox.currentIndex() == 0:
            self.levelValue = [1, 6]
        if self.comboBox.currentIndex() == 1:
            self.levelValue = [6, 12]
        if self.comboBox.currentIndex() == 2:
            self.levelValue = [12, 25]
        if self.comboBox.currentIndex() == 3:
            self.levelValue = [25, 100]

        self.lblSonuc.setText("")
        self.lblStatus.setText("")
        self.initializeRandoms()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    mainForm = QtGui.QWidget()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())

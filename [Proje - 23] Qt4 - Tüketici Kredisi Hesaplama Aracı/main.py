# -*- coding: utf-8 -*-

from __future__ import print_function

from PyQt4 import QtCore, QtGui

import scrapper

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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setGeometry(350, 10, 600, 600)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(19, 70, 561, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.labels(Form)

        self.comboBoxsAndLineedit()

        self.buttons(Form)

        self.tableArea(Form)

        self.resultArea(Form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Tüketici Kredisi Hesaplama Aracı", None))
        self.groupBox.setTitle(_translate("Form", "Kredi Bilgileri", None))
        self.label_2.setText(_translate("Form", "Almak İstediğiniz Kredi Türü", None))
        self.label_3.setText(_translate("Form", "Almak İstediğiniz Kredi Tutarı", None))
        self.label_4.setText(_translate("Form", "Ödeme Sıklığı", None))
        self.label_5.setText(_translate("Form", "Vade (Ay)", None))
        self.label_6.setText(_translate("Form", "Faiz Oranı(%)", None))
        self.btnHesapla.setText(_translate("Form", "Hesapla", None))
        self.btnTemizle.setText(_translate("Form", "Temizle", None))
        item = self.tableResult.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sıra", None))
        item = self.tableResult.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Taksit", None))
        item = self.tableResult.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Anapara", None))
        item = self.tableResult.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Faiz", None))
        item = self.tableResult.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Bakiye", None))
        item = self.tableResult.horizontalHeaderItem(5)
        item.setText(_translate("Form", "KKDF", None))
        item = self.tableResult.horizontalHeaderItem(6)
        item.setText(_translate("Form", "BSMV", None))

        self.txtFaiz.setPlaceholderText("x,xx")

        self.tableResult.setSortingEnabled(True)

        self.btnTemizleClicked()

    def tableArea(self, Form):
        self.tableResult = QtGui.QTableWidget(Form)
        self.tableResult.setGeometry(QtCore.QRect(15, 400, 571, 192))
        self.tableResult.setObjectName(_fromUtf8("tableResult"))
        self.tableResult.setColumnCount(7)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableResult.setHorizontalHeaderItem(6, item)

    def buttons(self, Form):
        self.btnHesapla = QtGui.QPushButton(Form)
        self.btnHesapla.setGeometry(QtCore.QRect(450, 300, 100, 41))
        self.btnHesapla.setAutoDefault(True)
        self.btnHesapla.setObjectName(_fromUtf8("btnHesapla"))
        self.btnTemizle = QtGui.QPushButton(Form)
        self.btnTemizle.setGeometry(QtCore.QRect(350, 300, 95, 41))
        self.btnTemizle.setObjectName(_fromUtf8("btnTemizle"))

        # Click Events
        self.btnHesapla.clicked.connect(self.btnHesaplaClicked)
        self.btnTemizle.clicked.connect(self.btnTemizleClicked)

    def labels(self, Form):
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 201, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 201, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 201, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(340, 110, 201, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(340, 180, 91, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))

    def resultArea(self, Form):
        self.gbSonuclar = QtGui.QGroupBox(Form)
        self.gbSonuclar.setGeometry(QtCore.QRect(20, 279, 291, 101))
        self.gbSonuclar.setTitle(_fromUtf8(""))
        self.gbSonuclar.setVisible(False)
        self.gbSonuclar.setObjectName(_fromUtf8("gbSonuclar"))
        self.lblFaiz = QtGui.QLabel(self.gbSonuclar)
        self.lblFaiz.setGeometry(QtCore.QRect(20, 60, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblFaiz.setFont(font)
        self.lblFaiz.setObjectName(_fromUtf8("lblFaiz"))
        self.lblTaksit = QtGui.QLabel(self.gbSonuclar)
        self.lblTaksit.setGeometry(QtCore.QRect(20, 30, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTaksit.setFont(font)
        self.lblTaksit.setObjectName(_fromUtf8("lblTaksit"))

    def comboBoxsAndLineedit(self):
        self.cbKt = QtGui.QComboBox(self.groupBox)
        self.cbKt.setGeometry(QtCore.QRect(20, 60, 201, 27))
        self.cbKt.setObjectName(_fromUtf8("cbKt"))
        self.cbOs = QtGui.QComboBox(self.groupBox)
        self.cbOs.setGeometry(QtCore.QRect(20, 130, 201, 27))
        self.cbOs.setObjectName(_fromUtf8("cbOs"))
        self.cbVade = QtGui.QComboBox(self.groupBox)
        self.cbVade.setGeometry(QtCore.QRect(340, 130, 201, 27))
        self.cbVade.setObjectName(_fromUtf8("cbVade"))

        self.txtKtu = QtGui.QLineEdit(self.groupBox)
        self.txtKtu.setGeometry(QtCore.QRect(340, 60, 201, 27))
        self.txtKtu.setObjectName(_fromUtf8("txtKtu"))
        self.txtFaiz = QtGui.QLineEdit(self.groupBox)
        self.txtFaiz.setGeometry(QtCore.QRect(440, 175, 101, 27))
        self.txtFaiz.setObjectName(_fromUtf8("txtFaiz"))

        self.addItemToComboBoxs()

    def addItemToComboBoxs(self):
        self.krediTuru = {
            "Masrafsiz Tuketici Kredisi": "G1",
            "Tuketici Kredisi": "G11",
            "Ipotekli Bireysel Finansman Kredisi": "G12",
            "Biz Tuketici Kredisi": "G17",
            "Biz Masrafsiz Tuketici Kredisi": "G18",
            "Calisan Biz Tuketici Kredisi": "G24",
            "Calisan Biz Masrafsiz Tuketici Kredisi": "G25",
            "Emekli Biz Tuketici Kredisi": "G27",
            "Emekli Biz Masrafsiz Tuketici Kredisi": "G28",
            "Oyak Uyelerine Ozel Tuketici Kredisi": "G30",
            "Arsa Kredisi": "G5",
            "Egitim Kredisi": "G6"
        }

        self.odemeSikligi = {
            "Ayda Bir": "1",
            "Uc Ayda Bir": "3"
        }

        self.cbKt.addItems([s for s in self.krediTuru.keys()])
        self.cbOs.addItems([s for s in self.odemeSikligi.keys()])
        self.cbVade.addItems([str(s) for s in range(1, 37)])

    def btnTemizleClicked(self):
        self.txtFaiz.setText("")
        self.txtKtu.setText("")
        self.cbVade.setCurrentIndex(0)
        self.cbKt.setCurrentIndex(0)
        self.cbOs.setCurrentIndex(0)
        self.gbSonuclar.setVisible(False)

    def btnHesaplaClicked(self):
        self.kt = self.krediTuru[str(self.cbKt.currentText())]
        self.s = self.odemeSikligi[str(self.cbOs.currentText())]
        self.v = str(self.cbVade.currentText())
        self.ktu = str(self.txtKtu.text())
        self.f = str(self.txtFaiz.text())

        self.getResultsAndAddToTable()

    def getResultsAndAddToTable(self):
        scrap = scrapper.Scrapper(self.kt, self.ktu, self.v, self.f, self.s)
        for i in scrap.getTable():
            for c, j in enumerate(range(0, len(i))):
                self.gbSonuclar.setVisible(True)
                self.lblTaksit.setText(_translate("Form", "Taksit Tutarı : {}".format(i[j]['Taksit']), None))
                self.lblFaiz.setText(_translate("Form", "Faiz Oranı      : {}".format(str(self.txtFaiz.text())), None))

                self.tableResult.setRowCount(len(i))
                self.tableResult.setItem(c, 0, QtGui.QTableWidgetItem(str(i[j]['Sira'])))
                self.tableResult.setItem(c, 1, QtGui.QTableWidgetItem(str(i[j]['Taksit'])))
                self.tableResult.setItem(c, 2, QtGui.QTableWidgetItem(str(i[j]['Anapara'])))
                self.tableResult.setItem(c, 3, QtGui.QTableWidgetItem(str(i[j]['Faiz'])))
                self.tableResult.setItem(c, 4, QtGui.QTableWidgetItem(str(i[j]['Bakiye'])))
                self.tableResult.setItem(c, 5, QtGui.QTableWidgetItem(str(i[j]['KKDF'])))
                self.tableResult.setItem(c, 6, QtGui.QTableWidgetItem(str(i[j]['BSMV'])))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

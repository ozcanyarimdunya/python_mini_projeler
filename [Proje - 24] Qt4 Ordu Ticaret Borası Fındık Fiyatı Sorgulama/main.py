# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from scrapper import Scrapper

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
    def setupUi(self, mainForm):
        # Main Windows
        mainForm.setObjectName(_fromUtf8("mainForm"))
        mainForm.resize(500, 364)

        # Need this
        self.date = QtCore.QDate(QtCore.QDate.currentDate())

        # Calendar Widget
        self.calendarWidget = QtGui.QCalendarWidget(mainForm)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 70, 480, 172))
        self.calendarWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.clicked[QtCore.QDate].connect(self.showSelectedDate)
        self.calendarWidget.setGridVisible(True)

        # Label Title
        self.lblTitle = QtGui.QLabel(mainForm)
        self.lblTitle.setGeometry(QtCore.QRect(10, 20, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))

        # Label_1
        self.label_1 = QtGui.QLabel(mainForm)
        self.label_1.setGeometry(QtCore.QRect(20, 270, 41, 20))
        self.label_1.setObjectName(_fromUtf8("label_1"))

        # Label Date
        self.lblDate = QtGui.QLabel(mainForm)
        self.lblDate.setGeometry(QtCore.QRect(90, 270, 101, 20))
        self.lblDate.setObjectName(_fromUtf8("lblDate"))

        # Button Result
        self.btnResult = QtGui.QPushButton(mainForm)
        self.btnResult.setGeometry(QtCore.QRect(20, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnResult.setFont(font)
        self.btnResult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnResult.setDefault(True)
        self.btnResult.setObjectName(_fromUtf8("btnResult"))
        # Result Button Clicked
        self.btnResult.clicked.connect(self.result)

        # Label Result
        self.lblResult = QtGui.QLabel(mainForm)
        self.lblResult.setGeometry(QtCore.QRect(240, 270, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblResult.setFont(font)
        self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResult.setObjectName(_fromUtf8("lblResult"))

        # ##
        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(_translate("mainForm", "Form", None))
        self.lblTitle.setText(_translate("mainForm", "Ordu Ticaret Borsası Fındık Fiyatı Sorgulama", None))
        self.label_1.setText(_translate("mainForm", "Tarih :", None))
        self.btnResult.setText(_translate("mainForm", "Sorgula", None))
        self.lblDate.setText(str(self.date.day()) + "/" + str(self.date.month()) + "/" + str(self.date.year()))

    # Show selected day in label date when clicked
    def showSelectedDate(self, _date):
        self.date = QtCore.QDate(_date)
        self.lblDate.setText(str(self.date.day()) + "/" + str(self.date.month()) + "/" + str(self.date.year()))

    def result(self):
        self.lblResult.setText("")
        scrap = Scrapper(self.date.year(), self.date.month(), self.date.day())
        self.lblResult.setText(str(scrap.getPrice()))


# Main
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    mainForm = QtGui.QWidget()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())

import sys

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QComboBox, QLabel, \
    QDoubleSpinBox, QPushButton, QTabWidget, QWidget, QTableWidgetItem, QTableWidget
from scrapper import get_data


class CreditThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def __init__(self, amount, maturity, product_type):
        super().__init__()
        self.amount = amount
        self.maturity = maturity
        self.product_type = product_type

    def run(self):
        self.onStart.emit("Loading credits ..")

        credit = get_data(self.amount, self.maturity, self.product_type)
        self.onScrapping.emit(credit)

        self.onFinish.emit('')


class MainWindow(QMainWindow):
    tbl_result: QTableWidget
    tab_widget: QTabWidget
    widget_calculator: QWidget
    tab_ihtiyac: QWidget
    tab_konut: QWidget
    tab_tasit: QWidget
    tab_kobi: QWidget
    lbl_amount: QLabel
    sb_amount: QDoubleSpinBox
    lbl_maturity: QLabel
    cb_maturity: QComboBox
    btn_calculate: QPushButton
    statusbar: QStatusBar
    credit_thread: CreditThread
    mappings = (
        ("ihtiyac", "tab_ihtiyac"),
        ("konut", "tab_konut"),
        ("tasit", "tab_tasit"),
        ("kobi", "tab_kobi"),
    )

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)
        self.initialise()

    def initialise(self):
        self.tab_widget.currentChanged.connect(lambda index: self.on_tab_change(index))
        self.btn_calculate.clicked.connect(lambda: self.on_calculate_clicked())

    def set_credits(self, amount, maturity, product_type):
        self.credit_thread = CreditThread(amount, maturity, product_type)
        self.credit_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.credit_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.credit_thread.onScrapping.connect(lambda credit: self.on_scrapped_credits(credit))
        self.credit_thread.start()

    def on_scrapped_credits(self, credit: list):
        """

        """
        self.tbl_result.setColumnCount(5)
        self.tbl_result.setRowCount(len(credit))

        self.tbl_result.setHorizontalHeaderLabels([
            "Banka",
            "Kredi Adı",
            "Faiz Oranı",
            "Toplam Maliyet",
            "Aylık Taksit",
        ])
        self.tbl_result.setIconSize(QSize(60, 60))
        self.tbl_result.setSortingEnabled(True)

        for row, data in enumerate(credit):
            item = QTableWidgetItem()
            item.setIcon(QIcon(data.get('logo')))

            self.tbl_result.setItem(row, 0, item)
            self.tbl_result.setItem(row, 1, QTableWidgetItem(data.get('BankName')))
            self.tbl_result.setItem(row, 2, QTableWidgetItem(data.get('InterestRate')))
            self.tbl_result.setItem(row, 3, QTableWidgetItem(data.get('TotalPaybackAmnt') + " TL"))
            self.tbl_result.setItem(row, 4, QTableWidgetItem(data.get('MonthlyInstallment') + " TL"))

    def on_tab_change(self, index):
        tab = getattr(self, self.mappings[index][1])
        self.widget_calculator.setParent(tab)
        self.widget_calculator.show()

    def on_calculate_clicked(self):
        current_tab = self.tab_widget.currentIndex()
        amount = int(self.sb_amount.value())
        maturity = int(self.cb_maturity.currentText())
        product_type = self.mappings[current_tab][0]
        self.set_credits(amount, maturity, product_type)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

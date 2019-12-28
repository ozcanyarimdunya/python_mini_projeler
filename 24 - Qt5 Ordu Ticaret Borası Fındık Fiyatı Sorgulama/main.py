import sys

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, \
    QPushButton, QCalendarWidget
from scrapper import get_data


class ScrapperThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def __init__(self, year, month, day):
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def run(self):
        self.onStart.emit("Loading credits ..")

        data = get_data(self.year, self.month, self.day)
        self.onScrapping.emit(data)

        self.onFinish.emit('')


class MainWindow(QMainWindow):
    cw_date: QCalendarWidget
    btn_query: QPushButton
    lbl_result: QLabel
    scrapper_thread: ScrapperThread

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)
        self.initialise()

    def initialise(self):
        self.btn_query.clicked.connect(lambda: self.on_query())

    def set_scrapping(self, year, month, day):
        self.scrapper_thread = ScrapperThread(year, month, day)
        self.scrapper_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.scrapper_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.scrapper_thread.onScrapping.connect(lambda credit: self.on_scrapped(credit))
        self.scrapper_thread.start()

    def on_scrapped(self, data: list):
        if len(data) > 1:
            self.lbl_result.setText(str(data[1]) + " TL")
        else:
            self.lbl_result.setText("Veri Yok!")

    def on_query(self):
        selected_date: QDate = self.cw_date.selectedDate()
        self.set_scrapping(
            year=selected_date.year(),
            month=selected_date.month(),
            day=selected_date.day()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

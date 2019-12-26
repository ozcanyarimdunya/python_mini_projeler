import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QComboBox, QLabel, QLineEdit

LEVELS = {
    "Kolay": (1, 6),
    "Orta": (6, 12),
    "Zor": (12, 25),
    "Çok Zor": (25, 100),
}


def get_randoms(level):
    start, end = LEVELS[level]
    num1 = randint(start, end)
    num2 = randint(start, end)
    return num1, num2


class MainWindow(QMainWindow):
    cb_level: QComboBox
    lbl_num1: QLabel
    lbl_num2: QLabel
    lbl_result: QLabel
    txt_result: QLineEdit
    statusbar: QStatusBar
    num1: int = 0
    num2: int = 0
    current_level = 'Kolay'

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)
        self.initialise()

    def initialise(self):
        self.cb_level.currentTextChanged.connect(
            lambda txt: self.on_level_changed(txt)
        )
        self.txt_result.returnPressed.connect(lambda: self.on_result_entered())
        self.txt_result.setFocus()
        self.start()

    def on_level_changed(self, txt):
        self.current_level = txt
        self.start()

    def start(self):
        self.num1, self.num2 = get_randoms(level=self.current_level)
        self.lbl_num1.setText(str(self.num1))
        self.lbl_num2.setText(str(self.num2))

    def on_result_entered(self):
        correct_answer = str(self.num1 * self.num2)
        user_answer = self.txt_result.text()
        self.txt_result.setText('')

        if correct_answer == user_answer:
            result = "{}x{}={}".format(
                self.num1, self.num2, correct_answer
            )
            self.lbl_result.setStyleSheet('color: green')
        else:
            result = "{}x{}={} >> {}".format(
                self.num1, self.num2, user_answer, correct_answer
            )
            self.lbl_result.setStyleSheet('color: red')
        self.lbl_result.setText(result)

        self.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

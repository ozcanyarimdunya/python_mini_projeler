import json
import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLineEdit,
    QListWidget,
    QListWidgetItem
)


class AppMainWindow(QMainWindow):
    txt_search: QLineEdit
    lw_list: QListWidget
    list_data = list()

    _path_form = 'ui/form.ui'
    _path_all = 'data/all.json'
    _path_checked = 'data/checked.json'

    def __init__(self, flags=None, *args, **kwargs):
        """
        Initialize the flags.

        Args:
            self: (todo): write your description
            flags: (int): write your description
        """
        super().__init__(flags, *args, **kwargs)
        self.initialise()

    def initialise(self):
        """
        Initialize the widget.

        Args:
            self: (todo): write your description
        """
        self.initialise_ui()
        self.initialise_data()
        self.initialise_event()
        self.initialise_widgets()

    def initialise_ui(self):
        """
        Initializes ui.

        Args:
            self: (todo): write your description
        """
        with open(self.path_form) as fp:
            uic.loadUi(self.path_form, self)

    def initialise_data(self):
        """
        Initialise the list of json files in path.

        Args:
            self: (todo): write your description
        """
        with open(self.path_all, 'r') as fp_all, open(self.path_checked) as fp_checked:
            _all = json.load(fp_all)
            _checked = json.load(fp_checked)
            self.list_data = list(
                map(lambda item:
                    dict(check_state=Qt.Checked, text=item) if item in _checked
                    else dict(check_state=Qt.Unchecked, text=item),
                    _all)
            )

    def initialise_event(self):
        """
        Initialize event handler

        Args:
            self: (todo): write your description
        """
        self.txt_search.textChanged.connect(lambda q: self.on_search(q))
        self.lw_list.itemChanged.connect(lambda item: self.on_lw_changed(item))

    def initialise_widgets(self):
        """
        Initialise all widgets

        Args:
            self: (todo): write your description
        """
        self.update_lw(data=self.list_data)

    def update_lw(self, data):
        """
        Updates the lw list

        Args:
            self: (todo): write your description
            data: (todo): write your description
        """
        self.lw_list.clear()
        for each in data:
            item = QListWidgetItem()
            item.setText(each['text'])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(each['check_state'])
            self.lw_list.addItem(item)

    def on_lw_changed(self, item: QListWidgetItem):
        """
        Called when a key changed

        Args:
            self: (todo): write your description
            item: (todo): write your description
        """
        self.list_data = list(
            map(lambda each:
                dict(check_state=item.checkState(), text=item.text()) if each['text'] == item.text() else each,
                self.list_data)
        )

    def on_search(self, query):
        """
        Add a new search.

        Args:
            self: (todo): write your description
            query: (str): write your description
        """
        data = list(
            filter(lambda q:
                   q['text'].lower().__contains__(query.lower()),
                   self.list_data)
        )
        self.update_lw(data)

    def closeEvent(self, event):
        """
        Close the list of items in the list.

        Args:
            self: (todo): write your description
            event: (todo): write your description
        """
        mapped = list(
            map(lambda item:
                item['text'],
                filter(lambda item: item['check_state'] == Qt.Checked, self.list_data))
        )
        with open(self._path_checked, 'w') as fp:
            json.dump(mapped, fp)

    @property
    def path_form(self):
        """
        Return true if the given path exists.

        Args:
            self: (todo): write your description
        """
        if not os.path.isfile(self._path_all):
            raise Exception('Cannot start without a ui file')
        return self._path_form

    @property
    def path_all(self):
        """
        Return a list of all of the path.

        Args:
            self: (todo): write your description
        """
        if not os.path.isfile(self._path_all):
            with open(self._path_all, 'w') as fp:
                json.dump([], fp)
        return self._path_all

    @property
    def path_checked(self):
        """
        Return a json - formatted contents of a json file.

        Args:
            self: (todo): write your description
        """
        if not os.path.isfile(self._path_checked):
            with open(self._path_checked, 'w') as fp:
                json.dump([], fp)
        return self._path_checked


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AppMainWindow()
    form.show()
    sys.exit(app.exec_())

import sys

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QComboBox, QListWidget
from scrapper import get_channels, get_streams


class ChannelsThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def run(self):
        self.onStart.emit("Loading channels ..")

        channels = get_channels()
        self.onScrapping.emit(channels)

        self.onFinish.emit('')


class StreamsThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        self.onStart.emit("Loading streams ..")

        streams = get_streams(self.url)
        self.onScrapping.emit(streams)

        self.onFinish.emit('')


class MainWindow(QMainWindow):
    cb_channels: QComboBox
    lw_streams: QListWidget
    statusbar: QStatusBar
    channels_thread: ChannelsThread
    streams_thread: StreamsThread
    channels = list()

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)
        self.initialise()

    def initialise(self):
        self.set_channels()
        self.cb_channels.currentIndexChanged.connect(
            lambda i: self.set_streams(self.channels[i]['url'])
        )

    def set_channels(self):
        self.channels_thread = ChannelsThread()
        self.channels_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.channels_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.channels_thread.onScrapping.connect(lambda channels: self.on_scrapped_channels(channels))
        self.channels_thread.start()

    def set_streams(self, url):
        self.streams_thread = StreamsThread(url)
        self.streams_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.streams_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.streams_thread.onScrapping.connect(lambda streams: self.on_scrapped_streams(streams))
        self.streams_thread.start()

    def on_scrapped_channels(self, channels):
        self.channels = channels
        for channel in self.channels:
            self.cb_channels.addItem(channel['name'])

    def on_scrapped_streams(self, streams):
        self.lw_streams.clear()
        data = []
        for stream in streams:
            data.append(
                "[{}] {} ({})".format(
                    stream['time'], stream['name'], stream['type']
                )
            )

        self.lw_streams.addItems(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

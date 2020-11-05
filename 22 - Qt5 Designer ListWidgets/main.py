import sys

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QListWidget, QListWidgetItem, QLabel, \
    QGraphicsView
from scrapper import get_channels, get_streams


class ChannelsThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def run(self):
        """
        Emits the channel.

        Args:
            self: (todo): write your description
        """
        self.onStart.emit("Loading channels ..")

        channels = get_channels()
        self.onScrapping.emit(channels)

        self.onFinish.emit('')


class StreamsThread(QThread):
    onStart = pyqtSignal(str)
    onScrapping = pyqtSignal(list)
    onFinish = pyqtSignal(str)

    def __init__(self, url):
        """
        Initialize the url.

        Args:
            self: (todo): write your description
            url: (str): write your description
        """
        super().__init__()
        self.url = url

    def run(self):
        """
        Emits the stream

        Args:
            self: (todo): write your description
        """
        self.onStart.emit("Loading streams ..")

        streams = get_streams(self.url)
        self.onScrapping.emit(streams)

        self.onFinish.emit('')


class MainWindow(QMainWindow):
    lw_channels: QListWidget
    lw_streams: QListWidget
    lbl_name: QLabel
    lbl_logo: QLabel
    gw_logo: QGraphicsView
    statusbar: QStatusBar
    channels_thread: ChannelsThread
    streams_thread: StreamsThread
    channels = list()

    def __init__(self, flags=None, *args, **kwargs):
        """
        Initialize this class.

        Args:
            self: (todo): write your description
            flags: (int): write your description
        """
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)
        self.initialise()

    def initialise(self):
        """
        Initialise the channel.

        Args:
            self: (todo): write your description
        """
        self.set_channels()
        self.lw_channels.itemClicked.connect(
            lambda item: self.set_streams(self.channels[self.lw_channels.currentRow()])
        )

    def set_channels(self):
        """
        Set the channel channels.

        Args:
            self: (todo): write your description
        """
        self.channels_thread = ChannelsThread()
        self.channels_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.channels_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.channels_thread.onScrapping.connect(lambda channels: self.on_scrapped_channels(channels))
        self.channels_thread.start()

    def set_streams(self, channel):
        """
        Set all the streams on the channel

        Args:
            self: (todo): write your description
            channel: (todo): write your description
        """
        url = channel['url']
        name = channel['name']
        logo = channel['logo']
        self.lbl_name.setText(name)
        self.lbl_logo.setPixmap(QPixmap(logo))

        self.streams_thread = StreamsThread(url)
        self.streams_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))
        self.streams_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))
        self.streams_thread.onScrapping.connect(lambda streams: self.on_scrapped_streams(streams))
        self.streams_thread.start()

    def on_scrapped_channels(self, channels):
        """
        When the channel is clicked.

        Args:
            self: (todo): write your description
            channels: (int): write your description
        """
        self.channels = channels
        for channel in self.channels:
            item = QListWidgetItem()
            item.setText(channel['name'])
            item.setIcon(QIcon(channel['logo']))
            self.lw_channels.addItem(item)

    def on_scrapped_streams(self, streams):
        """
        Add streams on streams

        Args:
            self: (todo): write your description
            streams: (todo): write your description
        """
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

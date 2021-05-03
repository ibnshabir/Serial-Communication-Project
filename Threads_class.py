from PyQt5.QtCore import QThread


class Threads(QThread):
    def __init__(self):
        super(Threads, self).__init__()

    def test_thread(self):
        print('testing Threads...')
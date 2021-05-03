from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Clients(QObject):
    display = pyqtSignal(str)

    def __init__(self, port):

        super(Clients, self).__init__()

        self.port = port

        self.port.write.connect(self.receive_data)

    def send_data(self):
        client_data = 'hello'
        self.port.read.emit(client_data)

    @pyqtSlot(str)
    def receive_data(self, port_data):
        self.display.emit(port_data)
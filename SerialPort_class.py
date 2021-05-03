from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QIODevice


class SerialPort(QObject):
    read = pyqtSignal(str)
    write = pyqtSignal(str)

    def __init__(self):
        super(SerialPort, self).__init__()

        self.port = QSerialPort()
        super().__init__()
        self.port.setPortName('/dev/pts/0')
        self.port.setBaudRate(QSerialPort.Baud115200)

        self.port.open(QIODevice.ReadWrite)  # opening port in read and write mode

        # signals
        self.read.connect(self.read_data)
        self.port.readyRead.connect(self.read_from_terminal)  # important in order to receive data from terminal

    @pyqtSlot(str)
    def read_data(self, client_data):
        print(f'Client: {client_data}')
        self.write_to_terminal(client_data)

    def write_to_terminal(self, client_data):
        self.port.write(bytes(client_data, 'utf-8'))  # the terminal accepts bytes, therefore converting it

    @pyqtSlot()
    def read_from_terminal(self):         # this method invoked automatically when data received from terminal
        terminal_data = self.port.readAll()
                                        # data sent by terminal is bytearray type, therefore need to convert into string
                                        # to convert data into string need to do the following
                                        # bytearray -> byte -> string
        byte_obj = bytes(terminal_data)
        converted_data = byte_obj.decode()

        self.write_data(converted_data)

    def write_data(self, converted_data):
        self.write.emit(converted_data)

    def moveToThread(self, thread: 'QThread') -> None:
        super(SerialPort, self).moveToThread(thread)
        self.port.moveToThread(thread)


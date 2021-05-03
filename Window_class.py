from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtCore import pyqtSlot
import sys


class Window(QDialog):

    def __init__(self, client):
        super(Window, self).__init__()

        self.setGeometry(10, 10, 500, 400)
        self.setWindowTitle('client window')

        self.send = QLabel('waiting to send...', self)
        self.send.setGeometry(50, 25, 250, 50)

        self.receive = QLabel('waiting to receive...', self)
        self.receive.setGeometry(50, 85, 250, 50)

        self.send_button = QPushButton('send data', self)
        self.send_button.setGeometry(100, 300, 150, 25)

        self.cancel = QPushButton('cancel', self)
        self.cancel.setGeometry(300, 300, 150, 25)
        self.cancel.clicked.connect(sys.exit)

        self.user_input = QLineEdit('try to send user input from here... ', self)
        self.user_input.setGeometry(50, 200, 400, 80)

        self.client = client
        self.send_button.clicked.connect(self.client.send_data)
        self.client.display.connect(self.display_input)
        self.client.port.read.connect(self.display_output)

        self.show()

    def user_input(self):
        pass

    @pyqtSlot(str)
    def display_input(self, port_data):
        print(f'Terminal: {port_data}')
        self.receive.setText(port_data)

    @pyqtSlot(str)
    def display_output(self, client_data):
        self.send.setText(client_data)
















'''
    - Why is my program closing when i close the window?
'''

from PyQt5.QtWidgets import QApplication
import sys
from Threads_class import Threads
from Clients_class import Clients
from Window_class import Window
from SerialPort_class import SerialPort

if __name__ == "__main__":
    app = QApplication(sys.argv)

    serial_port = SerialPort()
    client_1 = Clients(serial_port)
    window = Window(client_1)
    thread_1 = Threads()
    thread_1.start()
    serial_port.moveToThread(thread_1)

    sys.exit(app.exec_())

from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('myui.ui', self)
        self.show()

        self.mainstacked = self.findChild(QtWidgets.QStackedWidget, 'mainpages')
        self.ip_scan_button = self.findChild(QtWidgets.QPushButton, 'ipscanbutton')
        self.enum_button = self.findChild(QtWidgets.QPushButton, 'enumbutton')
        self.finger_button = self.findChild(QtWidgets.QPushButton, 'serverbutton')
        self.task_button = self.findChild(QtWidgets.QPushButton, 'newtaskbutton')

        # self.button.setText('test')
        self.ip_scan_button.clicked.connect(self.jump_to_ip_scan)
        self.enum_button.clicked.connect(self.jump_to_enum)
        self.finger_button.clicked.connect(self.jump_to_finger)
        self.task_button.clicked.connect(self.jump_to_task)

    def jump_to_ip_scan(self):
        self.mainstacked.setCurrentIndex(0)

    def jump_to_enum(self):
        self.mainstacked.setCurrentIndex(1)

    def jump_to_finger(self):
        self.mainstacked.setCurrentIndex(2)

    def jump_to_task(self):
        self.mainstacked.setCurrentIndex(3)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
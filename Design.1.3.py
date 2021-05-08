from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QProcess, QThread,QMutex, QReadWriteLock
import sys
import requests
import re
import time


# task class
class Task(QThread):
    def __init__(self, proc, args):
        super(Task, self).__init__()
        self.proc = proc
        self.args = args

    def run(self):
        mytask = QProcess()
        mytask.execute(self.proc, self.args)


queue = [("proc", "args"), ("nmap", "-sV"), ("nmap", "-sV")]
queuemutex = QReadWriteLock()


class WorkThread(QThread):
    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        while True:
            if len(queue) != 0:
                print("current queue: " + str(queue))
                time.sleep(5) # execute proc
                queuemutex.lockForWrite()
                temp = queue.pop(len(queue) - 1)
                queuemutex.unlock()
                print("task {} finished and deleted".format(temp))
                print(queue)


        print("thread start")
        print(queue)
        print("thread end")


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('myui.ui', self)
        self.show()

        self.t = WorkThread()

        self.mainstacked = self.findChild(QtWidgets.QStackedWidget, 'mainpages')
        self.ip_scan_button = self.findChild(QtWidgets.QPushButton, 'ipscanbutton')
        self.enum_button = self.findChild(QtWidgets.QPushButton, 'enumbutton')
        self.finger_button = self.findChild(QtWidgets.QPushButton, 'serverbutton')
        self.task_button = self.findChild(QtWidgets.QPushButton, 'newtaskbutton')

        # enum_input
        self.enum_input = self.findChild(QtWidgets.QLineEdit, 'enuminput')
        self.enum_start = self.findChild(QtWidgets.QPushButton, 'enumstart')
        self.enum_list = self.findChild(QtWidgets.QTextBrowser,  'enumshow')

        self.enum_start.clicked.connect(self.start_enum)


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

    def start_enum(self):
        domain = self.enum_input.text()
        self.enum_list.append(domain)
        #self.t = MyThread()
        self.t.start()
        queuemutex.lockForWrite()
        queue.append(("enum", domain))
        queuemutex.unlock()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
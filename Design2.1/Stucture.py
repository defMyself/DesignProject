from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QProcess, QThread, QMutex, QReadWriteLock
import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import requests
import re
import time
import enumfrombaidu


# task class
class Task(QThread):
    def __init__(self, proc, args):
        super(Task, self).__init__()
        self.proc = proc
        self.args = args

    def run(self):
        mytask = QProcess()
        mytask.execute(self.proc, self.args)


work_queue = [("python", "test.py"), ("python", "enumfrombaidu.py v.zzu.edu.cn"), ("whois", "baidu.com")]
current_work_queue = [("python", "test.py"), ("python", "enumfrombaidu.py v.zzu.edu.cn"), ("whois", "baidu.com")]
queuemutex = QReadWriteLock()


# monitor task queue and execute new task
class ServerThread(QThread):
    def __init__(self):
        super(ServerThread, self).__init__()

    def run(self):
        while True:
            if len(current_work_queue) != 0:
                print("current queue: " + str(current_work_queue))
                print("next task: ", end='')
                # execute task
                self.execute_task()

                # after current task finished, delete it from current_work_queue
                queuemutex.lockForWrite()
                try:
                    temp = current_work_queue.pop(len(current_work_queue)- 1)
                except:
                    print("pop error")

                queuemutex.unlock()
                #print(temp)
                #print("task {} finished and deleted".format(temp))
                print(current_work_queue)

        print("thread start")
        print(queue)
        print("thread end")

    def execute_task(self):

        temp = current_work_queue.pop()
        task_name = temp[1]
        #enumfrombaidu.getdomainsfrombaidu(task_name)

        #args = []
        #args.append(temp[1])
        #p.execute('python', ['enumfrombaidu.py'])
        print("success")
        #print(str(p.readAll(), encoding='u8'))

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('myui.ui', self)
        self.show()
        self.setupUi()

        self.server_thread = ServerThread()
        self.server_thread.start()


    def setupUi(self):
        self.mainstacked = self.findChild(QtWidgets.QStackedWidget, 'mainpages')
        self.ip_scan_button = self.findChild(QtWidgets.QPushButton, 'ipscanbutton')
        self.enum_button = self.findChild(QtWidgets.QPushButton, 'enumbutton')
        self.finger_button = self.findChild(QtWidgets.QPushButton, 'serverbutton')
        self.task_button = self.findChild(QtWidgets.QPushButton, 'newtaskbutton')

        # enum_input
        self.enum_input = self.findChild(QtWidgets.QLineEdit, 'enuminput')
        self.enum_start = self.findChild(QtWidgets.QPushButton, 'enumstart')
        self.enum_list = self.findChild(QtWidgets.QTextBrowser, 'enumshow')

        self.enum_start.clicked.connect(self.start_enum)
        self.enum_input.text()

        # self.button.setText('test')
        self.ip_scan_button.clicked.connect(self.jump_to_ip_scan)
        self.enum_button.clicked.connect(self.jump_to_enum)
        self.finger_button.clicked.connect(self.jump_to_finger)
        self.task_button.clicked.connect(self.jump_to_task)

        # tableWIdget
        self.history_table = self.findChild(QtWidgets.QTableWidget, 'historytable')
        self.domain_table = self.findChild(QtWidgets.QTableView, "domaintable")
        self.model = QStandardItemModel(2,2)
        self.model.setHorizontalHeaderLabels(['domain', 'ip'])
        self.model.setItem(0,0, QStandardItem("test"))
        self.show_db_button = self.findChild(QtWidgets.QPushButton, 'showdb')
        self.show_db_button.clicked(self.show_db)
        self.domain_table.setModel(self.model)

        self.history_table.setRowCount(5)
        self.history_table.setColumnCount(4)
        self.history_table.setHorizontalHeaderLabels(["id", "task name", "domain"])
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
        self.enum_list.append("add a new enum task: " + domain)

        work_queue.append(("python", " enum_name.py " + domain))
        queuemutex.lockForWrite()
        current_work_queue.append(("python", "enum_name.py " + domain))
        queuemutex.unlock()
        
    def show_db(self):
        pass


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QProcess, QThread
import sys
import requests
import re


# task class
class Task(QThread):
    def __init__(self, proc, args):
        super(Task, self).__init__()
        self.proc = proc
        self.args = args

    def run(self):
        mytask = QProcess()
        mytask.execute(self.proc, self.args)



class MyThread(QThread):
    def __init__(self, url):
        super(MyThread, self).__init__()
        self.url = url

    def test_process(self):
        proc = QProcess()
        proc.start('python3', ["/home/kali/Desktop/Sublist3r/sublist3r.py", '-d', 'v.zzu.edu.cn'])
        proc.execute('python3 /home/kali/Desktop/Sublist3r/sublist3r.py -d v.zzu.edu.cn')
        proc.start('python3', ['/home/kali/Desktop/Sublist3r/sublist3r.py', '-d', 'www.v.zzu.edu.cn'])
        proc.execute('whatweb baidu.com')
        proc.start('touch test.txt')
        proc.execute('nmap' ,['baidu.com'])
        proc.waitForFinished()
        result = str(proc.readAllStandardOutput())
        proc.execute('dnsenum ')

    def run(self):
        res = requests.get(self.url)
        reresult = re.findall(r"http://.*?\.com|http://.*?\.cn|https://.*?\.com|https://.*?\.cn", res.text)
        reemail = re.findall(r" *?@.*?", res.text)
        print(reemail)
        for d in set(reresult):
            print(d)
        print(len(reresult))
        print(len(set(reresult)))
        print("hhhh")


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('myui.ui', self)
        self.show()
        # thread as a member, execute domain enum task
        self.t = MyThread("http://www.zzu.edu.cn")

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
        print("start enum")
        domain = self.enum_input.text()
        self.enum_list.append(domain)
        #self.t = MyThread()
        self.t.start()
        #self.t.wait()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
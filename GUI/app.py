import sys
from PyQt5.QtWidgets import *


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi()

    def setupUi(self):

        self.resize(512, 512)
        self.status = self.statusBar()
        self.status.showMessage("status", 4000)
        self.setWindowTitle('Hacking tools')
        self.move_center()

        #
        #self.text_browser = QTextBrowser(self)
        #self.text_browser.setText('kkk')

        # add button
        button1 = QPushButton("domain enum", self)
        button1.setChecked(True)
        button1.clicked.connect(domain_enum)
        button1.move(20, 50)

        button2 = QPushButton("ip scan", self)
        button2.setChecked(True)
        button2.clicked.connect(ip_scan)
        button2.move(20, 85)

        button3 = QPushButton("vuln scan", self)
        button3.setChecked(True)
        button3.clicked.connect(vuln_scan)
        button3.move(20, 120)

        button4 = QPushButton("setting", self)
        button4.setChecked(True)
        button4.clicked.connect(setting)
        button4.move(20, 155)
        # add line
        e1 = QLineEdit("Line Edit", self)
        e1.move(120, 50)


        # e1.setMaxLength(4)

        # add input
        # text_edit = QTextEdit(self)
        # text_edit.setText("test input")
        #text_edit.append("test")
        # text_edit.move(130, 50)
        # self.text = text_edit.toPlainText()

        # add label
        #label = QLabel(self)
        #label.setText("input domain")
        #text = label.text()


    def clicked_function(self):
        print(self.text)

    def move_center(self):
        screen = QDesktopWidget().screenGeometry()
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) / 2
        y_move_step = (screen.height() - form.height()) / 2
        self.move(x_move_step, y_move_step)


def clicked_function():
    print('press button1...')


def ip_scan():
    print("start ip scan")


def domain_enum():
    print("start domain enum")


def vuln_scan():
    print("start vuln scan")


def setting():
    print("setting")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

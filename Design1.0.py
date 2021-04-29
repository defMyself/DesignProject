import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # 界面初始化
        # 主界面设置
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage("status", 4000)
        self.setWindowTitle('Hacking tools')
        self.move_center()
        self.setWindowIcon(QIcon("./Kitty Mac.ico"))

        # 域名枚举模块 启动按钮
        button1 = QPushButton("域名枚举", self)
        button1.setChecked(True)
        button1.clicked.connect(self.domain_enum)
        button1.move(20, 50)

        # 输入域名
        self.domain_enum_input = QLineEdit("zzu.edu.cn", self)
        self.domain_enum_input.move(120, 50)

        # ip扫描按钮
        button2 = QPushButton("ip 扫描", self)
        button2.setChecked(True)
        button2.clicked.connect(self.ip_scan)
        button2.move(20, 85)

        # 输入ip
        self.ip_scan_input = QLineEdit("192.168.1.102", self)
        self.ip_scan_input.move(120, 85)

        button3 = QPushButton("指纹识别", self)
        button3.setChecked(True)
        button3.clicked.connect(self.vuln_scan)
        button3.move(20, 120)

        # 输入ip
        self.domain_enum_input = QLineEdit("www.zzu.edu.cn", self)
        self.domain_enum_input.move(120, 120)

        button4 = QPushButton("系统配置", self)
        button4.setChecked(True)
        button4.clicked.connect(self.setting)
        button4.move(20, 155)

        # 显示框
        self.text_brower = QTextBrowser(self)
        self.text_brower.move(400, 60)
        self.text_brower.resize(300, 500)

    def display_line(self):
        input_domain = self.e1.text()
        print(input_domain)

        # e1.setMaxLength(4)

        # add input
        # text_edit = QTextEdit(self)
        # text_edit.setText("test input")
        # text_edit.append("test")
        # text_edit.move(130, 50)
        # self.text = text_edit.toPlainText()

        # add label
        # label = QLabel(self)
        # label.setText("input domain")
        # text = label.text()

    def clicked_function(self):
        print(self.text)

    def move_center(self):
        screen = QDesktopWidget().screenGeometry()
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) / 2
        y_move_step = (screen.height() - form.height()) / 2
        self.move(x_move_step, y_move_step)

    def ip_scan(self):
        print("start ip scan")

    def domain_enum(self):
        print("start domain enum")

    def vuln_scan(self):
        print("start vuln scan")

    def setting(self):
        print("setting")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

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
        #
        self.move_center()

        # 
        self.text_browser = QTextBrowser(self)
        self.text_browser.setText('kkk')
        
     
        # add button
        button1 = QPushButton(self)
        button1.setChecked(True)
        button1.clicked.connect(clicked_function)

    def clicked_function(self):
        print("button was clicked...")

    def move_center(self):
        screen = QDesktopWidget().screenGeometry()
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) / 2
        y_move_step = (screen.height() - form.height()) / 2
        self.move(x_move_step, y_move_step)

def clicked_function():
    print('press button1...')

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

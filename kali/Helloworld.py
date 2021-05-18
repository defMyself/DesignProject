import sys
import Hello
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
Myapp = Hello.Ui_MainWindow()

sys.exit(app.exec())
# dynamic load
# -*- coding: GBK-*- #
import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QTabWidget, QTabBar


class TabWidget(QTabWidget):
    def __init__(self, txt='none', list=['a', 'b'], widgetList=[QWidget(), QWidget()], parent=None):
        super(TabWidget, self).__init__(parent)
        self.text = txt
        self.tabList = list
        self.widgetList = widgetList
        if len(list) != len(widgetList):
            return
        print(1)
        for index, perTab in enumerate(list):
            print('x')
            self.addTab(widgetList[index], perTab)

    def resizeEvent(self, event):
        # super().paintEvent(event)
        total_width = self.width()
        count = len(self.tabList)
        if count > 0:
            per_width = total_width / count
            str_stylesheet = "QTabBar::tab{width:%dpx;height:30px;border-style: solid; border-width: 1px 1px 1px 1px;background:white;color:black;border-top-left-radius:6px;border-top-right-radius:6px;}QTabBar::tab:selected{border-style: solid; border-width: 1px 1px 1px 1px;border-bottom-color:white;background:white;color:black;}" % per_width
            self.setStyleSheet(str_stylesheet)


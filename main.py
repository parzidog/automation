
# CREATOR: KENNETH A SCHAEFER II
# V:0.0.7

import sys
import platform
import PyQt5
from PyQt5 import QtCore, QtWidgets  # , QtGui
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
#from PyQt5 import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_window_functions import *
from wichita_falls_fun import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW MAIN WINDOW
        self.show()

    # APP EVENTS
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #APP FUNCTIONS
    def appFunctions(self):  # , wichita_falls_fun):
        self.wichita_falls.clicked.connect(clickme(WF))

        # def clickme(button_click):
        #     button_click = wichita_falls_fun


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

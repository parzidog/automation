
# CREATOR: KENNETH A SCHAEFER II
# V:0.0.7

import sys
# import platform
# import PyQt5
# from PyQt5 import QtCore, QtWidgets  # , QtGui
# from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
# from PyQt5 import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
# from PyQt5.QtWidgets import QApplication

# GUI FILE
import ui_main

# IMPORT FUNCTIONS
import ui_window_functions
import wichita_falls_fun


class MainWindow(ui_window_functions.QMainWindow, ui_main.Ui_MainWindow, wichita_falls_fun.wichitaFalls):
    def __init__(self):
        ui_window_functions.QMainWindow.__init__(self)
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if self.UIFunctions.returnStatus() == 1:
                self.UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == ui_window_functions.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        # ==> SET UI DEFINITIONS
        ui_window_functions.UIFunctions.uiDefinitions(self)

        # SHOW MAIN WINDOW
        self.show()

    # APP EVENTS
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = ui_window_functions.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

##############################
#
# BY: KENNETH A SCHAEFER II
# V:0.0.1
#
##############################

#GUI FILE
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ui_main
from QtGui import QColor, QGraphics, QSizeGrip


## ==> GLOBALS

GLOBAL_STATE = 0


class UIFunctions(Ui_MainWindow):

    #   ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.dropShadowFrame.setContentsMargins(0, 0, 0, 0)
            self.ui.dropShadowFrame.setStyleSheet(
                "background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.4375 rgba(25, 25, 25, 255), stop:1 rgba(81, 81, 81, 255));border-radius: 0px;")
            self.ui.maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.dropShadowFrame.setContentsMargins(10, 10, 10, 10)
            self.ui.dropShadowFrame.setStyleSheet(
                "background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.4375 rgba(25, 25, 25, 255), stop:1 rgba(81, 81, 81, 255));border-radius: 10px;")
            self.ui.maximize.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphics.DropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.maximize.clicked.connect(
            lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED

    def returnStatus():
        return GLOBAL_STATE


# CREATOR: KENNETH A SCHAEFER II
# V:0.0.7

import sys
import platform
import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QSizeGrip, QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

# GUI FILE
import ui_main
import amarillo
import austin
import caddo_mills
import dallas
import enid
import ennis
import gresham1
import gresham2
import hobbs
import kaufman
import kaufman_2
import krum
import laughlin
import lindale
import lubbock
import mineola
import mineola_2
import paris
import seminole
import stillwater
import tulsa
import wichita_falls_fun

# GLOBALS
GLOBAL_STATE = 0


class UIFunctions(QMainWindow):

    # MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    # UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTOREs
        self.ui.btn_maximize.clicked.connect(
            lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(20,20,20) }")
        self.sizegrip.setToolTip("Resize Window")

        # BUTTON CLICKS
        self.ui.amarillo.clicked.connect(
            lambda: amarillo.hobbs.getReports())
        self.ui.austin.clicked.connect(lambda: austin.hobbs.getReports())
        self.ui.caddo_mills.clicked.connect(
            lambda: caddo_mills.hobbs.getReports())
        self.ui.dallas.clicked.connect(lambda: dallas.hobbs.getReports())
        self.ui.enid.clicked.connect(lambda: enid.hobbs.getReports())
        self.ui.ennis.clicked.connect(lambda: ennis.hobbs.getReports())
        self.ui.gresham.clicked.connect(lambda: gresham1.hobbs.getReports())
        self.ui.mineola2.clicked.connect(
            lambda: gresham2.hobbs.getReports())
        self.ui.hobbs.clicked.connect(lambda: hobbs.hobbs.getReports())
        self.ui.kaufman.clicked.connect(lambda: kaufman.hobbs.getReports())
        self.ui.kaufman2.clicked.connect(
            lambda: kaufman_2.hobbs.getReports())
        self.ui.krum.clicked.connect(lambda: krum.hobbs.getReports())
        self.ui.laughlin.clicked.connect(
            lambda: laughlin.hobbs.getReports())
        self.ui.lindale.clicked.connect(lambda: lindale.hobbs.getReports())
        self.ui.lubbock.clicked.connect(lambda: lubbock.hobbs.getReports())
        self.ui.mineola.clicked.connect(lambda: mineola.hobbs.getReports())
        self.ui.mineola2.clicked.connect(
            lambda: mineola_2.hobbs.getReports())
        self.ui.paris.clicked.connect(lambda: paris.hobbs.getReports())
        self.ui.hobbs.clicked.connect(
            lambda: seminole.hobbs.getReports())
        self.ui.stillwater.clicked.connect(
            lambda: stillwater.hobbs.getReports())
        self.ui.tulsa.clicked.connect(lambda: tulsa.hobbs.getReports())
        self.ui.wichita_falls.clicked.connect(
            lambda: wichita_falls_fun.hobbs.getReports())

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTORED

    def returnStatus():
        return GLOBAL_STATE

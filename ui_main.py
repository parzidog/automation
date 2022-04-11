
# CREATOR: KENNETH A SCHAEFER II
# V:0.0.7

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dropShadowLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.dropShadowLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowLayout.setSpacing(0)
        self.dropShadowLayout.setObjectName("dropShadowLayout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.4375 rgba(25, 25, 25, 255), stop:1 rgba(81, 81, 81, 255));\n"
                                             "border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.title = QtWidgets.QFrame(self.title_bar)
        self.title.setStyleSheet("background: none;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.title)
        self.horizontal_layout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontal_layout_2.setSpacing(0)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.frame = QtWidgets.QFrame(self.title)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_3.setSpacing(0)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.buttons = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setMaximumSize(QtCore.QSize(70, 30))
        self.buttons.setToolTipDuration(0)
        self.buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontal_layout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_4.setSpacing(0)
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.btn_close = QtWidgets.QPushButton(self.buttons)
        self.btn_close.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_close.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_close.setToolTipDuration(0)
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    color: #333;\n"
                                     "    border: 2px solid #555;\n"
                                     "    border-radius: 7px;\n"
                                     "    border-style: outset;\n"
                                     "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.272727 rgba(255, 40, 40, 255), stop:0.801136 rgba(81, 81, 81, 255));\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    border-radius: 7px;\n"
                                     "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.119318 rgba(81, 81, 81, 255), stop:0.744318 rgba(255, 40, 40, 255));\n"
                                     "}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontal_layout_4.addWidget(self.btn_close)
        self.btn_minimize = QtWidgets.QPushButton(self.buttons)
        self.btn_minimize.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_minimize.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_minimize.setMouseTracking(False)
        self.btn_minimize.setTabletTracking(False)
        self.btn_minimize.setAcceptDrops(False)
        self.btn_minimize.setToolTipDuration(0)
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "color: #333;\n"
                                        "border: 2px solid #555;\n"
                                        "border-radius: 7px;\n"
                                        "border-style: outset;\n"
                                        "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.267045 rgba(255, 255, 0, 255), stop:0.8125 rgba(81, 81, 81, 255));\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-radius: 7px;\n"
                                        "\n"
                                        "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0340909 rgba(81, 81, 81, 255), stop:0.664773 rgba(255, 255, 0, 255));\n"
                                        "}")
        self.btn_minimize.setText("")
        self.btn_minimize.setIconSize(QtCore.QSize(15, 15))
        self.btn_minimize.setShortcut("")
        self.btn_minimize.setFlat(False)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontal_layout_4.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.buttons)
        self.btn_maximize.setMinimumSize(QtCore.QSize(15, 15))
        self.btn_maximize.setMaximumSize(QtCore.QSize(15, 15))
        self.btn_maximize.setToolTipDuration(0)
        self.btn_maximize.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 7px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.295455 rgba(85, 255, 40, 255), stop:0.778409 rgba(81, 81, 81, 255));\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-radius: 7px;\n"
                                        "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.119318 rgba(81, 81, 81, 255), stop:0.744318 rgba(85, 255, 40, 255));\n"
                                        "}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontal_layout_4.addWidget(self.btn_maximize)
        self.horizontal_layout_3.addWidget(self.buttons)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(167000, 35))
        font = QtGui.QFont()
        font.setFamily("Blackadder ITC")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(255,255,255,255); padding: 3px;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignBottom
                                | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.horizontal_layout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(175, 30))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(235,0,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontal_layout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(40, 40))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\DJCSAppLogo.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontal_layout_3.addWidget(self.label_3)
        self.horizontal_layout_2.addWidget(self.frame)
        self.horizontal_layout.addWidget(self.title)
        self.vertical_layout.addWidget(self.title_bar)
        self.Aldeo = QtWidgets.QFrame(self.drop_shadow_frame)
        self.Aldeo.setMinimumSize(QtCore.QSize(100, 100))
        self.Aldeo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Aldeo.setToolTip("")
        self.Aldeo.setStyleSheet("background: none;")
        self.Aldeo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Aldeo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Aldeo.setObjectName("Aldeo")
        self.gridLayout = QtWidgets.QGridLayout(self.Aldeo)
        self.gridLayout.setObjectName("gridLayout")
        self.laughlin = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.laughlin.sizePolicy().hasHeightForWidth())
        self.laughlin.setSizePolicy(sizePolicy)
        self.laughlin.setMinimumSize(QtCore.QSize(100, 100))
        self.laughlin.setMaximumSize(QtCore.QSize(16777215, 150))
        self.laughlin.setSizeIncrement(QtCore.QSize(1, 1))
        self.laughlin.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.laughlin.setFont(font)
        self.laughlin.setStyleSheet("QPushButton{\n"
                                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                    "color: rgb(235, 235, 235);\n"
                                    "border: 0;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                    "color: rgba(235, 0, 0, 255);\n"
                                    "border: 0;\n"
                                    "}")
        self.laughlin.setIconSize(QtCore.QSize(16, 16))
        self.laughlin.setObjectName("laughlin")
        self.gridLayout.addWidget(self.laughlin, 6, 1, 1, 1)
        self.mineola_2 = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mineola_2.sizePolicy().hasHeightForWidth())
        self.mineola_2.setSizePolicy(sizePolicy)
        self.mineola_2.setMinimumSize(QtCore.QSize(100, 100))
        self.mineola_2.setMaximumSize(QtCore.QSize(150, 150))
        self.mineola_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.mineola_2.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.mineola_2.setFont(font)
        self.mineola_2.setStyleSheet("QPushButton{\n"
                                     "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                     "color: rgb(235, 235, 235);\n"
                                     "border: 0;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                     "color: rgba(235, 0, 0, 255);\n"
                                     "border: 0;\n"
                                     "}")
        self.mineola_2.setIconSize(QtCore.QSize(16, 16))
        self.mineola_2.setObjectName("mineola_2")
        self.gridLayout.addWidget(self.mineola_2, 6, 5, 1, 1)
        self.austin = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.austin.sizePolicy().hasHeightForWidth())
        self.austin.setSizePolicy(sizePolicy)
        self.austin.setMinimumSize(QtCore.QSize(100, 100))
        self.austin.setMaximumSize(QtCore.QSize(150, 150))
        self.austin.setSizeIncrement(QtCore.QSize(1, 1))
        self.austin.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.austin.setFont(font)
        self.austin.setStyleSheet("QPushButton{\n"
                                  "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                  "color: rgb(235, 235, 235);\n"
                                  "border: 0;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                  "color: rgba(235, 0, 0, 255);\n"
                                  "border: 0;\n"
                                  "}")
        self.austin.setIconSize(QtCore.QSize(16, 16))
        self.austin.setObjectName("austin")
        self.gridLayout.addWidget(self.austin, 4, 2, 1, 1)
        self.tulsa = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tulsa.sizePolicy().hasHeightForWidth())
        self.tulsa.setSizePolicy(sizePolicy)
        self.tulsa.setMinimumSize(QtCore.QSize(100, 100))
        self.tulsa.setMaximumSize(QtCore.QSize(150, 150))
        self.tulsa.setSizeIncrement(QtCore.QSize(1, 1))
        self.tulsa.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.tulsa.setFont(font)
        self.tulsa.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "color: rgba(235, 0, 0, 255);\n"
                                 "border: 0;\n"
                                 "}")
        self.tulsa.setIconSize(QtCore.QSize(16, 16))
        self.tulsa.setObjectName("tulsa")
        self.gridLayout.addWidget(self.tulsa, 7, 4, 1, 1)
        self.ennis = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ennis.sizePolicy().hasHeightForWidth())
        self.ennis.setSizePolicy(sizePolicy)
        self.ennis.setMinimumSize(QtCore.QSize(100, 100))
        self.ennis.setMaximumSize(QtCore.QSize(150, 150))
        self.ennis.setSizeIncrement(QtCore.QSize(1, 1))
        self.ennis.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ennis.setFont(font)
        self.ennis.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "color: rgba(235, 0, 0, 255);\n"
                                 "border: 0;\n"
                                 "}")
        self.ennis.setIconSize(QtCore.QSize(16, 16))
        self.ennis.setObjectName("ennis")
        self.gridLayout.addWidget(self.ennis, 5, 1, 1, 1)
        self.paris = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.paris.sizePolicy().hasHeightForWidth())
        self.paris.setSizePolicy(sizePolicy)
        self.paris.setMinimumSize(QtCore.QSize(100, 100))
        self.paris.setMaximumSize(QtCore.QSize(150, 150))
        self.paris.setSizeIncrement(QtCore.QSize(1, 1))
        self.paris.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.paris.setFont(font)
        self.paris.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "color: rgba(235, 0, 0, 255);\n"
                                 "border: 0;\n"
                                 "}")
        self.paris.setIconSize(QtCore.QSize(16, 16))
        self.paris.setObjectName("paris")
        self.gridLayout.addWidget(self.paris, 7, 1, 1, 1)
        self.lindale = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lindale.sizePolicy().hasHeightForWidth())
        self.lindale.setSizePolicy(sizePolicy)
        self.lindale.setMinimumSize(QtCore.QSize(100, 100))
        self.lindale.setMaximumSize(QtCore.QSize(150, 150))
        self.lindale.setSizeIncrement(QtCore.QSize(1, 1))
        self.lindale.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.lindale.setFont(font)
        self.lindale.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lindale.setStyleSheet("QPushButton{\n"
                                   "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                   "color: rgb(235, 235, 235);\n"
                                   "border: 0;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                   "color: rgba(235, 0, 0, 255);\n"
                                   "border: 0;\n"
                                   "}")
        self.lindale.setIconSize(QtCore.QSize(16, 16))
        self.lindale.setObjectName("lindale")
        self.gridLayout.addWidget(self.lindale, 6, 2, 1, 1)
        self.kaufman_2 = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.kaufman_2.sizePolicy().hasHeightForWidth())
        self.kaufman_2.setSizePolicy(sizePolicy)
        self.kaufman_2.setMinimumSize(QtCore.QSize(100, 100))
        self.kaufman_2.setMaximumSize(QtCore.QSize(150, 150))
        self.kaufman_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.kaufman_2.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.kaufman_2.setFont(font)
        self.kaufman_2.setStyleSheet("QPushButton{\n"
                                     "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                     "color: rgb(235, 235, 235);\n"
                                     "border: 0;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                     "color: rgba(235, 0, 0, 255);\n"
                                     "border: 0;\n"
                                     "}")
        self.kaufman_2.setIconSize(QtCore.QSize(16, 16))
        self.kaufman_2.setObjectName("kaufman_2")
        self.gridLayout.addWidget(self.kaufman_2, 5, 4, 1, 1)
        self.caddo_mills = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.caddo_mills.sizePolicy().hasHeightForWidth())
        self.caddo_mills.setSizePolicy(sizePolicy)
        self.caddo_mills.setMinimumSize(QtCore.QSize(100, 100))
        self.caddo_mills.setMaximumSize(QtCore.QSize(150, 150))
        self.caddo_mills.setSizeIncrement(QtCore.QSize(1, 1))
        self.caddo_mills.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.caddo_mills.setFont(font)
        self.caddo_mills.setStyleSheet("QPushButton{\n"
                                       "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                       "color: rgb(235, 235, 235);\n"
                                       "border: 0;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                       "color: rgba(235, 0, 0, 255);\n"
                                       "border: 0;\n"
                                       "}")
        self.caddo_mills.setIconSize(QtCore.QSize(16, 16))
        self.caddo_mills.setObjectName("caddo_mills")
        self.gridLayout.addWidget(self.caddo_mills, 4, 3, 1, 1)
        self.wichita_falls = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wichita_falls.sizePolicy().hasHeightForWidth())
        self.wichita_falls.setSizePolicy(sizePolicy)
        self.wichita_falls.setMinimumSize(QtCore.QSize(100, 100))
        self.wichita_falls.setMaximumSize(QtCore.QSize(150, 150))
        self.wichita_falls.setSizeIncrement(QtCore.QSize(1, 1))
        self.wichita_falls.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.wichita_falls.setFont(font)
        self.wichita_falls.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.wichita_falls.setStyleSheet("QPushButton{\n"
                                         "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                         "color: rgb(235, 235, 235);\n"
                                         "border: 0;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                         "color: rgba(235, 0, 0, 255);\n"
                                         "border: 0;\n"
                                         "}")
        self.wichita_falls.setIconSize(QtCore.QSize(16, 16))
        self.wichita_falls.setAutoDefault(False)
        self.wichita_falls.setDefault(True)
        self.wichita_falls.setFlat(False)
        self.wichita_falls.setObjectName("wichita_falls")
        self.gridLayout.addWidget(self.wichita_falls, 7, 5, 1, 1)
        self.krum = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.krum.sizePolicy().hasHeightForWidth())
        self.krum.setSizePolicy(sizePolicy)
        self.krum.setMinimumSize(QtCore.QSize(100, 100))
        self.krum.setMaximumSize(QtCore.QSize(16777215, 150))
        self.krum.setSizeIncrement(QtCore.QSize(1, 1))
        self.krum.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.krum.setFont(font)
        self.krum.setStyleSheet("QPushButton{\n"
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                "color: rgb(235, 235, 235);\n"
                                "border: 0;\n"
                                "}\n"
                                "\n"
                                "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                "color: rgba(235, 0, 0, 255);\n"
                                "border: 0;\n"
                                "}")
        self.krum.setIconSize(QtCore.QSize(16, 16))
        self.krum.setObjectName("krum")
        self.gridLayout.addWidget(self.krum, 5, 5, 1, 1)
        self.lubbock = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lubbock.sizePolicy().hasHeightForWidth())
        self.lubbock.setSizePolicy(sizePolicy)
        self.lubbock.setMinimumSize(QtCore.QSize(100, 100))
        self.lubbock.setMaximumSize(QtCore.QSize(150, 150))
        self.lubbock.setSizeIncrement(QtCore.QSize(1, 1))
        self.lubbock.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.lubbock.setFont(font)
        self.lubbock.setStyleSheet("QPushButton{\n"
                                   "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                   "color: rgb(235, 235, 235);\n"
                                   "border: 0;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                   "color: rgba(235, 0, 0, 255);\n"
                                   "border: 0;\n"
                                   "}")
        self.lubbock.setIconSize(QtCore.QSize(16, 16))
        self.lubbock.setObjectName("lubbock")
        self.gridLayout.addWidget(self.lubbock, 6, 3, 1, 1)
        self.dallas = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dallas.sizePolicy().hasHeightForWidth())
        self.dallas.setSizePolicy(sizePolicy)
        self.dallas.setMinimumSize(QtCore.QSize(100, 100))
        self.dallas.setMaximumSize(QtCore.QSize(150, 150))
        self.dallas.setSizeIncrement(QtCore.QSize(1, 1))
        self.dallas.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.dallas.setFont(font)
        self.dallas.setStyleSheet("QPushButton{\n"
                                  "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                  "color: rgb(235, 235, 235);\n"
                                  "border: 0;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                  "color: rgba(235, 0, 0, 255);\n"
                                  "border: 0;\n"
                                  "}")
        self.dallas.setIconSize(QtCore.QSize(16, 16))
        self.dallas.setObjectName("dallas")
        self.gridLayout.addWidget(self.dallas, 4, 4, 1, 1)
        self.enid = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.enid.sizePolicy().hasHeightForWidth())
        self.enid.setSizePolicy(sizePolicy)
        self.enid.setMinimumSize(QtCore.QSize(100, 100))
        self.enid.setMaximumSize(QtCore.QSize(16777215, 150))
        self.enid.setSizeIncrement(QtCore.QSize(1, 1))
        self.enid.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.enid.setFont(font)
        self.enid.setStyleSheet("QPushButton{\n"
                                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                "color: rgb(235, 235, 235);\n"
                                "border: 0;\n"
                                "}\n"
                                "\n"
                                "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                "color: rgba(235, 0, 0, 255);\n"
                                "border: 0;\n"
                                "}")
        self.enid.setIconSize(QtCore.QSize(16, 16))
        self.enid.setObjectName("enid")
        self.gridLayout.addWidget(self.enid, 4, 5, 1, 1)
        self.mineola = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mineola.sizePolicy().hasHeightForWidth())
        self.mineola.setSizePolicy(sizePolicy)
        self.mineola.setMinimumSize(QtCore.QSize(100, 100))
        self.mineola.setMaximumSize(QtCore.QSize(150, 150))
        self.mineola.setSizeIncrement(QtCore.QSize(1, 1))
        self.mineola.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.mineola.setFont(font)
        self.mineola.setStyleSheet("QPushButton{\n"
                                   "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                   "color: rgb(235, 235, 235);\n"
                                   "border: 0;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                   "color: rgba(235, 0, 0, 255);\n"
                                   "border: 0;\n"
                                   "}")
        self.mineola.setIconSize(QtCore.QSize(16, 16))
        self.mineola.setObjectName("mineola")
        self.gridLayout.addWidget(self.mineola, 6, 4, 1, 1)
        self.seminole = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.seminole.sizePolicy().hasHeightForWidth())
        self.seminole.setSizePolicy(sizePolicy)
        self.seminole.setMinimumSize(QtCore.QSize(100, 100))
        self.seminole.setMaximumSize(QtCore.QSize(150, 150))
        self.seminole.setSizeIncrement(QtCore.QSize(1, 1))
        self.seminole.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.seminole.setFont(font)
        self.seminole.setStyleSheet("QPushButton{\n"
                                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                    "color: rgb(235, 235, 235);\n"
                                    "border: 0;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                    "color: rgba(235, 0, 0, 255);\n"
                                    "border: 0;\n"
                                    "}")
        self.seminole.setIconSize(QtCore.QSize(16, 16))
        self.seminole.setObjectName("seminole")
        self.gridLayout.addWidget(self.seminole, 7, 2, 1, 1)
        self.hobbs = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hobbs.sizePolicy().hasHeightForWidth())
        self.hobbs.setSizePolicy(sizePolicy)
        self.hobbs.setMinimumSize(QtCore.QSize(100, 100))
        self.hobbs.setMaximumSize(QtCore.QSize(150, 150))
        self.hobbs.setSizeIncrement(QtCore.QSize(1, 1))
        self.hobbs.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.hobbs.setFont(font)
        self.hobbs.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "color: rgba(235, 0, 0, 255);\n"
                                 "border: 0;\n"
                                 "}")
        self.hobbs.setIconSize(QtCore.QSize(16, 16))
        self.hobbs.setObjectName("hobbs")
        self.gridLayout.addWidget(self.hobbs, 5, 2, 1, 1)
        self.stillwater = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stillwater.sizePolicy().hasHeightForWidth())
        self.stillwater.setSizePolicy(sizePolicy)
        self.stillwater.setMinimumSize(QtCore.QSize(100, 100))
        self.stillwater.setMaximumSize(QtCore.QSize(150, 150))
        self.stillwater.setSizeIncrement(QtCore.QSize(1, 1))
        self.stillwater.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.stillwater.setFont(font)
        self.stillwater.setStyleSheet("QPushButton{\n"
                                      "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                      "color: rgb(235, 235, 235);\n"
                                      "border: 0;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                      "color: rgba(235, 0, 0, 255);\n"
                                      "border: 0;\n"
                                      "}")
        self.stillwater.setIconSize(QtCore.QSize(16, 16))
        self.stillwater.setObjectName("stillwater")
        self.gridLayout.addWidget(self.stillwater, 7, 3, 1, 1)
        self.amarillo = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.amarillo.sizePolicy().hasHeightForWidth())
        self.amarillo.setSizePolicy(sizePolicy)
        self.amarillo.setMinimumSize(QtCore.QSize(100, 100))
        self.amarillo.setMaximumSize(QtCore.QSize(150, 150))
        self.amarillo.setSizeIncrement(QtCore.QSize(1, 1))
        self.amarillo.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.amarillo.setFont(font)
        self.amarillo.setStyleSheet("QPushButton{\n"
                                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                    "color: rgb(235, 235, 235);\n"
                                    "border: 0;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                    "color: rgba(235, 0, 0, 255);\n"
                                    "border: 0;\n"
                                    "}")
        self.amarillo.setIconSize(QtCore.QSize(16, 16))
        self.amarillo.setObjectName("amarillo")
        self.gridLayout.addWidget(self.amarillo, 4, 1, 1, 1)
        self.kaufman = QtWidgets.QPushButton(self.Aldeo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.kaufman.sizePolicy().hasHeightForWidth())
        self.kaufman.setSizePolicy(sizePolicy)
        self.kaufman.setMinimumSize(QtCore.QSize(100, 100))
        self.kaufman.setMaximumSize(QtCore.QSize(150, 150))
        self.kaufman.setSizeIncrement(QtCore.QSize(1, 1))
        self.kaufman.setBaseSize(QtCore.QSize(125, 125))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.kaufman.setFont(font)
        self.kaufman.setStyleSheet("QPushButton{\n"
                                   "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\ncolor: rgb(235, 235, 235);\\nborder: 0;\n"
                                   "color: rgb(235, 235, 235);\n"
                                   "border: 0;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:Hover{background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                   "color: rgba(235, 0, 0, 255);\n"
                                   "border: 0;\n"
                                   "}")
        self.kaufman.setIconSize(QtCore.QSize(16, 16))
        self.kaufman.setObjectName("kaufman")
        self.gridLayout.addWidget(self.kaufman, 5, 3, 1, 1)
        self.vertical_layout.addWidget(self.Aldeo)
        self.credits = QtWidgets.QFrame(self.drop_shadow_frame)
        self.credits.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits.setStyleSheet("background: none;")
        self.credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits.setObjectName("credits")
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout(self.credits)
        self.horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_5.setSpacing(0)
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        self.credits_2 = QtWidgets.QFrame(self.credits)
        self.credits_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_2.setObjectName("credits_2")
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout(self.credits_2)
        self.horizontal_layout_6.setObjectName("horizontal_layout_6")
        self.label_4 = QtWidgets.QLabel(self.credits_2)
        self.label_4.setStyleSheet("QLabel{\n"
                                   "color: rgba(0,0,0,0);\n"
                                   "}\n"
                                   "\n"
                                   "QLabel:Hover{\n"
                                   "color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(182, 55, 255, 255), stop:0.505682 rgba(0, 255, 0, 255), stop:0.75 rgba(182, 55, 255, 255));\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.horizontal_layout_6.addWidget(self.label_4)
        self.frame_2 = QtWidgets.QFrame(self.credits_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontal_layout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontal_layout_7.setObjectName("horizontal_layout_7")
        self.horizontal_layout_6.addWidget(self.frame_2)
        self.horizontal_layout_5.addWidget(self.credits_2)
        self.frame_grip = QtWidgets.QFrame(self.credits)
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontal_layout_5.addWidget(self.frame_grip)
        self.vertical_layout.addWidget(self.credits)
        self.dropShadowLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.label.setText(_translate("MainWindow", "Tocarro\'s"))
        self.label_2.setText(_translate("MainWindow", "Automation App"))
        self.laughlin.setText(_translate("MainWindow", "Laughlin"))
        self.mineola_2.setText(_translate("MainWindow", "Mineola 2"))
        self.austin.setText(_translate("MainWindow", "Austin"))
        self.tulsa.setText(_translate("MainWindow", "Tulsa"))
        self.ennis.setText(_translate("MainWindow", "Ennis"))
        self.paris.setText(_translate("MainWindow", "Paris"))
        self.lindale.setText(_translate("MainWindow", "Lindale"))
        self.kaufman_2.setText(_translate("MainWindow", "Kaufman 2"))
        self.caddo_mills.setText(_translate("MainWindow", "Caddo Mills"))
        self.wichita_falls.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p>WF</p></body></html>"))
        self.wichita_falls.setText(_translate("MainWindow", "Wichita Falls"))
        self.krum.setText(_translate("MainWindow", "Krum"))
        self.lubbock.setText(_translate("MainWindow", "Lubbock"))
        self.dallas.setText(_translate("MainWindow", "Dallas"))
        self.enid.setText(_translate("MainWindow", "Enid"))
        self.mineola.setText(_translate("MainWindow", "Mineola"))
        self.seminole.setText(_translate("MainWindow", "Seminole"))
        self.hobbs.setText(_translate("MainWindow", "Hobbs"))
        self.stillwater.setText(_translate("MainWindow", "Stillwater"))
        self.amarillo.setText(_translate("MainWindow", "Amarillo"))
        self.kaufman.setText(_translate("MainWindow", "Kaufman"))
        self.label_4.setText(_translate(
            "MainWindow", "Designed and Programmed by: Kenneth Schaefer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

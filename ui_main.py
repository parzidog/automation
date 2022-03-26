
# CREATOR: KENNETH A SCHAEFER II
# V:0.0.7


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(475, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1850, 1020))
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(1850, 50))
        self.title_bar.setStyleSheet("background: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setStyleSheet("background: none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_title)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_btns = QtWidgets.QFrame(self.frame)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 50))
        self.frame_btns.setToolTipDuration(1)
        self.frame_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btns.setLineWidth(0)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(18, 18))
        self.btn_close.setMaximumSize(QtCore.QSize(18, 18))
        self.btn_close.setMouseTracking(False)
        self.btn_close.setAcceptDrops(False)
        self.btn_close.setToolTip("Close")
        self.btn_close.setToolTipDuration(1)
        self.btn_close.setStyleSheet("QPushButton{\n"
                                     "    border-style: outset;\n"
                                     "    border: 2px solid #555;\n"
                                     "    border-radius: 9px;\n"
                                     "    background-color: rgba(255, 40, 40, 255);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    border-radius: 9px;\n"
                                     "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0340909 rgba(81, 81, 81, 255), stop:0.564773 rgba(255, 40, 40, 255));\n"
                                     "}\n"
                                     "")
        self.btn_close.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btn_close.setText("")
        self.btn_close.setShortcut("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(18, 18))
        self.btn_minimize.setMaximumSize(QtCore.QSize(18, 18))
        self.btn_minimize.setMouseTracking(False)
        self.btn_minimize.setTabletTracking(False)
        self.btn_minimize.setAcceptDrops(False)
        self.btn_minimize.setToolTip("Minimize")
        self.btn_minimize.setToolTipDuration(1)
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "color: #333;\n"
                                        "border-style: outset;\n"
                                        "border: 2px solid #555;\n"
                                        "border-radius: 9px;\n"
                                        "background-color: rgba(240, 200, 0, 255);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-radius: 9px;\n"
                                        "\n"
                                        "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0340909 rgba(81, 81, 81, 255), stop:0.564773 rgba(240, 200, 0, 255));\n"
                                        "}")
        self.btn_minimize.setText("")
        self.btn_minimize.setIconSize(QtCore.QSize(18, 18))
        self.btn_minimize.setShortcut("")
        self.btn_minimize.setFlat(False)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_4.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(18, 18))
        self.btn_maximize.setMaximumSize(QtCore.QSize(18, 18))
        self.btn_maximize.setToolTipDuration(1)
        self.btn_maximize.setToolTip("Maximize")
        self.btn_maximize.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 9px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color: rgba(85, 230, 40, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border-radius: 9px;\n"
                                        "    background-color: qradialgradient(pread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0340909 rgba(81, 81, 81, 255), stop:0.564773 rgba(85, 255, 40, 255));\n"
                                        "}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_4.addWidget(self.btn_maximize)
        self.horizontalLayout_3.addWidget(self.frame_btns)
        self.label_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QtCore.QSize(100, 30))
        self.label_title.setMaximumSize(QtCore.QSize(1850, 30))
        font = QtGui.QFont()
        font.setFamily("Blackadder ITC")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setStyleSheet(
            "color: rgba(255,255,255,255); padding: 3px;")
        self.label_title.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label_title.setIndent(0)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_3.addWidget(self.label_title)
        self.label_title2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_title2.sizePolicy().hasHeightForWidth())
        self.label_title2.setSizePolicy(sizePolicy)
        self.label_title2.setMinimumSize(QtCore.QSize(125, 25))
        self.label_title2.setMaximumSize(QtCore.QSize(1850, 25))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title2.setFont(font)
        self.label_title2.setStyleSheet("color:rgba(235,0,0,255);")
        self.label_title2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_title2.setObjectName("label_title2")
        self.horizontalLayout_3.addWidget(
            self.label_title2, 0, QtCore.Qt.AlignHCenter)
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMinimumSize(QtCore.QSize(30, 20))
        self.logo.setMaximumSize(QtCore.QSize(30, 20))
        self.logo.setStyleSheet("background: none;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../DJCSAppLogo0.png"))
        self.logo.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_title)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setMaximumSize(QtCore.QSize(1850, 1020))
        self.content_bar.setToolTip("")
        self.content_bar.setStyleSheet("background: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.gridLayout = QtWidgets.QGridLayout(self.content_bar)
        self.gridLayout.setObjectName("gridLayout")
        self.initial_setup = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.initial_setup.sizePolicy().hasHeightForWidth())
        self.initial_setup.setSizePolicy(sizePolicy)
        self.initial_setup.setMinimumSize(QtCore.QSize(100, 100))
        self.initial_setup.setMaximumSize(QtCore.QSize(150, 150))
        self.initial_setup.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.initial_setup.setFont(font)
        self.initial_setup.setTabletTracking(False)
        self.initial_setup.setStyleSheet("QPushButton{\n"
                                         "background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.0852273 rgba(25, 25, 25, 255), stop:0.335227 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                         "color: rgba(235, 0, 0, 255);\n"
                                         "border: 0;\n"
                                         "}\n"
                                         "QPushButton:Hover{\n"
                                         "color: rgba(25,25,25,1);\n"
                                         "    background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.113636 rgba(255, 40, 40, 255), stop:0.352273 rgba(207, 207, 207, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                         "}")
        self.initial_setup.setObjectName("initial_setup")
        self.gridLayout.addWidget(self.initial_setup, 2, 2, 1, 1)
        self.site3 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site3.sizePolicy().hasHeightForWidth())
        self.site3.setSizePolicy(sizePolicy)
        self.site3.setMinimumSize(QtCore.QSize(100, 100))
        self.site3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site3.setFont(font)
        self.site3.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site3.setObjectName("site3")
        self.gridLayout.addWidget(self.site3, 3, 3, 1, 1)
        self.site5 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site5.sizePolicy().hasHeightForWidth())
        self.site5.setSizePolicy(sizePolicy)
        self.site5.setMinimumSize(QtCore.QSize(100, 100))
        self.site5.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site5.setFont(font)
        self.site5.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site5.setObjectName("site5")
        self.gridLayout.addWidget(self.site5, 4, 2, 1, 1)
        self.site6 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site6.sizePolicy().hasHeightForWidth())
        self.site6.setSizePolicy(sizePolicy)
        self.site6.setMinimumSize(QtCore.QSize(100, 100))
        self.site6.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site6.setFont(font)
        self.site6.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.site6.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site6.setObjectName("site6")
        self.gridLayout.addWidget(self.site6, 4, 3, 1, 1)
        self.site8 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site8.sizePolicy().hasHeightForWidth())
        self.site8.setSizePolicy(sizePolicy)
        self.site8.setMinimumSize(QtCore.QSize(100, 100))
        self.site8.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site8.setFont(font)
        self.site8.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site8.setObjectName("site8")
        self.gridLayout.addWidget(self.site8, 5, 2, 1, 1)
        self.site9 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site9.sizePolicy().hasHeightForWidth())
        self.site9.setSizePolicy(sizePolicy)
        self.site9.setMinimumSize(QtCore.QSize(100, 100))
        self.site9.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site9.setFont(font)
        self.site9.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site9.setObjectName("site9")
        self.gridLayout.addWidget(self.site9, 5, 3, 1, 1)
        self.site7 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site7.sizePolicy().hasHeightForWidth())
        self.site7.setSizePolicy(sizePolicy)
        self.site7.setMinimumSize(QtCore.QSize(100, 100))
        self.site7.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site7.setFont(font)
        self.site7.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site7.setObjectName("site7")
        self.gridLayout.addWidget(self.site7, 5, 1, 1, 1)
        self.site4 = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.site4.sizePolicy().hasHeightForWidth())
        self.site4.setSizePolicy(sizePolicy)
        self.site4.setMinimumSize(QtCore.QSize(100, 100))
        self.site4.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.site4.setFont(font)
        self.site4.setStyleSheet("QPushButton{\n"
                                 "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                 "color: rgb(235, 235, 235);\n"
                                 "border: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:Hover{\n"
                                 "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                 "}")
        self.site4.setObjectName("site4")
        self.gridLayout.addWidget(self.site4, 4, 1, 1, 1)
        self.amarillo = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.amarillo.sizePolicy().hasHeightForWidth())
        self.amarillo.setSizePolicy(sizePolicy)
        self.amarillo.setMinimumSize(QtCore.QSize(100, 100))
        self.amarillo.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.amarillo.setFont(font)
        self.amarillo.setStyleSheet("QPushButton{\n"
                                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                    "color: rgb(235, 235, 235);\n"
                                    "border: 0;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:Hover{\n"
                                    "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                    "}")
        self.amarillo.setObjectName("amarillo")
        self.gridLayout.addWidget(self.amarillo, 3, 2, 1, 1)
        self.wichita_falls = QtWidgets.QPushButton(self.content_bar)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wichita_falls.sizePolicy().hasHeightForWidth())
        self.wichita_falls.setSizePolicy(sizePolicy)
        self.wichita_falls.setMinimumSize(QtCore.QSize(100, 100))
        self.wichita_falls.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wichita_falls.setFont(font)
        self.wichita_falls.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.wichita_falls.setStyleSheet("QPushButton{\n"
                                         "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.494318, stop:0.35 rgba(235, 0, 0, 255), stop:1 rgba(0,0,0,0), stop:1 rgba(0,0,0,0));\\n color: rgb(235, 235, 235);\\n border: 0;\n"
                                         "color: rgb(235, 235, 235);\n"
                                         "border: 0;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:Hover{\n"
                                         "color: #000000; background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.758, fx:0.5, fy:0.494, stop:0.107955 rgba(207, 207, 207, 255), stop:0.335227 rgba(255, 40, 40, 255), stop:0.636364 rgba(25, 25, 25, 0));\n"
                                         "}")
        self.wichita_falls.setAutoDefault(False)
        self.wichita_falls.setDefault(True)
        self.wichita_falls.setFlat(False)
        self.wichita_falls.setObjectName("wichita_falls")
        self.gridLayout.addWidget(self.wichita_falls, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.content_bar)
        self.credits = QtWidgets.QFrame(self.drop_shadow_frame)
        self.credits.setMinimumSize(QtCore.QSize(200, 30))
        self.credits.setMaximumSize(QtCore.QSize(1850, 30))
        self.credits.setStyleSheet("background: none;")
        self.credits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits.setObjectName("credits")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.credits)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.credits_2 = QtWidgets.QFrame(self.credits)
        self.credits_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_2.setStyleSheet("background: none;")
        self.credits_2.setObjectName("credits_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.credits_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.credits_2)
        self.label_4.setMinimumSize(QtCore.QSize(160, 40))
        self.label_4.setMaximumSize(QtCore.QSize(1850, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.label_4.setStyleSheet("QLabel{\n"
                                   "color: rgba(0,0,0,0);\n"
                                   "}\n"
                                   "\n"
                                   "QLabel:Hover{\n"
                                   "color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(182, 55, 255, 255), stop:0.505682 rgba(0, 255, 0, 255), stop:0.75 rgba(182, 55, 255, 255));\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.credits_2)
        self.frame_grip = QtWidgets.QFrame(self.credits)
        self.frame_grip.setMinimumSize(QtCore.QSize(20, 20))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding: 5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_5.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits)
        self.dropShadowLayout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.label_title.setText(_translate("MainWindow", "Tocarro\'s"))
        self.label_title2.setText(_translate("MainWindow", "Automation App"))
        self.initial_setup.setText(_translate("MainWindow", "Initial Setup"))
        self.site3.setText(_translate("MainWindow", "Site 3"))
        self.site5.setText(_translate("MainWindow", "Site 5"))
        self.site6.setText(_translate("MainWindow", "Site 6"))
        self.site8.setText(_translate("MainWindow", "Site 8"))
        self.site9.setText(_translate("MainWindow", "Site 9"))
        self.site7.setText(_translate("MainWindow", "Site 7"))
        self.site4.setText(_translate("MainWindow", "Site 4"))
        self.amarillo.setText(_translate("MainWindow", "Amarillo"))
        self.wichita_falls.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p>WF</p></body></html>"))
        self.wichita_falls.setText(_translate("MainWindow", "Wichita Falls"))
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

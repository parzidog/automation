import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStyleSheet("background: black;")
        
        self.setupGUI()

    def setupGUI(self):
        super().__init__()
        self.setWindowTitle("WSS Automation")

        self.wf = QPushButton("Wichita Falls", QMainWindow)
        self.amarillo = QPushButton("Amarillo")
        self.littleRock = QPushButton("Little Rock")
        self.dallas = QPushButton("Dallas")

        #Grid Layout
        box = QGridLayout()
        box.addWidget(self.wf, 0, 0)
        box.addWidget(self.amarillo, 0, 1)
        box.addWidget(self.littleRock, 1, 0)
        box.addWidget(self.dallas, 1, 1)

        self.setLayout(box)
        self.setStyleSheet("background: black;")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    app.exec()

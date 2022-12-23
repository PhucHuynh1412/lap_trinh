from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt


import sys 

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")
        self.button = QPushButton("Push Me")
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(self.button)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


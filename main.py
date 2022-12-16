from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("A first Program with PySide6")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()

app.exec_()



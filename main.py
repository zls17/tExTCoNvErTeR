from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QPushButton, QTextEdit, QWidget)
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Converter")
        self.resize(600, 500)
        self.textEntry = QTextEdit()
        self.textEntry.setFont(QFont("Menlo", 24))
        self.convertButton = QPushButton("Convert")
        self.convertButton.setFont(QFont("Comic Sans MS", 24))
        self.outputEntry = QTextEdit()
        self.outputEntry.setFont(QFont("Menlo", 24))
        self.copyButton = QPushButton("Copy")
        self.copyButton.setFont(QFont("Menlo", 24))
        layout = QVBoxLayout()
        layout.addWidget(self.textEntry)
        layout.addWidget(self.convertButton)
        layout.addWidget(self.outputEntry)
        layout.addWidget(self.copyButton)
        widget = QWidget()
        widget.setLayout(layout)
        self.convertButton.pressed.connect(self.convert)
        self.copyButton.pressed.connect(self.copy)
        self.setCentralWidget(widget)
        self.show()
    def convert(self):
        self.outputText = ""
        text = self.textEntry.toPlainText()
        count = 0
        for char in text:
            if count % 2 == 0:
                self.outputText += char.upper()
                count += 1
            else:
                self.outputText += char
                count += 1

        self.outputEntry.setText(self.outputText)

    def copy(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.outputText, mode=cb.Clipboard)
        
app = QApplication([])
window = MainWindow()
app.exec()
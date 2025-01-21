# module imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QBoxLayout, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App object and settings

        self.setWindowTitle("Calculator App")
        self.resize(400, 600)

        # Create all App widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Calibri", 24))


        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        self.clear_button = QPushButton("C")
        self.delete_button = QPushButton("DEL")

        self.create_buttons()
        self.create_layout()
        self.clear_button.setStyleSheet("QPushButton { font-size: 24px comic-sans; padding: 10px }")
        self.delete_button.setStyleSheet("QPushButton { font-size: 24px comic-sans; padding: 10px }")

    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                result = eval(symbol)
                self.text_box.setText(str(result))

            except Exception as e:
                print("Error", e)

        elif text == "C":
            self.text_box.clear()

        elif text == "DEL":
            text = self.text_box.text()[:-1]
            self.text_box.setText(text)

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)

    def create_buttons(self):
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton { font-size: 24px comic-sans; padding: 10px }")
            self.grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

    def create_layout(self):
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QVBoxLayout()
        button_row.addWidget(self.clear_button)
        button_row.addWidget(self.delete_button)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(master_layout)

        self.clear_button.clicked.connect(self.button_click)
        self.delete_button.clicked.connect(self.button_click)


# Run App
app = QApplication([])
main_window = CalculatorApp()
main_window.setStyleSheet(" Object {background-color: #f0f0f0}")
main_window.show()
app.exec_()
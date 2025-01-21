#module imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QBoxLayout, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

#Main App object and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(400, 600)

#Create all App objects
text_box = QLineEdit()
grid = QGridLayout()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

clear_button = QPushButton("C")
delete_button = QPushButton("DEL")

def button_click():
  button = app.sender()
  text = button.text()

  if text == "=":
    symbol = text_box.text()
    try:
      result = eval(symbol)
      text_box.setText(str(result))

    except Exception as e:
      text_box.setText("Error", e)

  elif text == "C":
    text_box.clear()


row = 0
col = 0

for text in buttons:
  button = QPushButton(text)
  # button.clicked.connect(none)
  grid.addWidget(button, row, col)
  col += 1

  if col > 3:
    col = 0
    row += 1

#Create Design Layout

master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
# master_layout.addLayout(grid)
master_layout.addLayout(grid)

button_row = QVBoxLayout()
button_row.addWidget(clear_button)
button_row.addWidget(delete_button)

master_layout.addLayout(button_row)

# Set the master layout to the main window
main_window.setLayout(master_layout)
#Events

#Run App
main_window.show()
app.exec_()

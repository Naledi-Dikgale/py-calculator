# Scientific Calculator

This is a Python-based scientific calculator built using the Tkinter library for the graphical user interface and NumPy for mathematical functions.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Scientific functions: sine, cosine, tangent, logarithm, and square root.
- Supports both degrees and radians for trigonometric functions.
- Constants: π (pi) and e (Euler's number).
- Clear (C) and delete (DEL) functionalities.
- Toggle between degrees and radians.

## Installation

1. Clone the repository:
  ```sh
  git clone https://github.com/Naledi-Dikgale/py-calculator.git
  ```
2. Navigate to the project directory:
  ```sh
  cd py-calculator
  ```
3. Install the required dependencies:
  ```sh
  pip install numpy
  ```

## Usage

Run the calculator application:
```sh
python calculator.py
```

## Code Overview

The main components of the calculator are:

- **CalculatorApp Class**: Inherits from `tk.Tk` and sets up the main window and widgets.
- **create_widgets Method**: Creates and arranges the buttons and display entry.
- **on_button_click Method**: Handles button click events and performs calculations.

## License

This project is licensed under the MIT License.

import tkinter as tk
from tkinter import font as tkfont
import numpy as np

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.configure(bg="#ffe4e1")  # Light pink background
        self.resizable(True, True)

        self.is_degree = True  # Track current mode (degrees or radians)

        self.create_widgets()

    def create_widgets(self):
        # Display Entry (spans entire width)
        self.display = tk.Entry(self, font=tkfont.Font(size=24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Scientific Buttons
        sci_buttons = [
            "sin", "cos", "tan", "log", "√",
            "(", ")", "π", "e", "ˆ"
        ]
        row = 1
        col = 0
        for button in sci_buttons:
            action = lambda x=button: self.on_button_click(x)
            b = tk.Button(self, text=button, font=tkfont.Font(size=16), bg="#bbdefb", fg="black", relief="raised", command=action)
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Main Calculator Buttons
        buttons = [
            "7", "8", "9", "÷", "C",
            "4", "5", "6", "×", "DEL",
            "1", "2", "3", "−", "",
            "0", ".", "=", "+"
        ]

        row += 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            bg_color = "#f8bbd0"  # Default button color
            if button in ("C", "DEL"):
                bg_color = "#a5d6a7"  # Light green
            b = tk.Button(self, text=button, font=tkfont.Font(size=18), bg=bg_color, fg="black", relief="raised", command=action)
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Rad/Deg Button at the Bottom
        action = lambda: self.on_button_click("Deg/Rad")
        rad_deg_button = tk.Button(self, text="Deg/Rad", font=tkfont.Font(size=18), bg="#ffcc80", fg="black", relief="raised", command=action)
        rad_deg_button.grid(row=row + 1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Grid Configurations
        for i in range(5):
            self.grid_columnconfigure(i, weight=1, uniform="col")
        for i in range(row + 2):
            self.grid_rowconfigure(i, weight=1, uniform="row")

    def on_button_click(self, char):
        if char == "=":
            try:
                expression = self.display.get()
                expression = expression.replace("÷", "/").replace("×", "*").replace("ˆ", "**").replace("√", "sqrt")
                result = eval(expression, {"__builtins__": None}, {
                    "sin": lambda x: np.sin(np.deg2rad(x)) if self.is_degree else np.sin(x),
                    "cos": lambda x: np.cos(np.deg2rad(x)) if self.is_degree else np.cos(x),
                    "tan": lambda x: np.tan(np.deg2rad(x)) if self.is_degree else np.tan(x),
                    "log": np.log,
                    "sqrt": np.sqrt,
                    "pi": np.pi,
                    "e": np.e
                })
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == "C":
            self.display.delete(0, tk.END)
        elif char == "DEL":
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text[:-1])
        elif char == "Deg/Rad":
            self.is_degree = not self.is_degree
            mode = "Degrees" if self.is_degree else "Radians"
            print(f"Mode switched to {mode}")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

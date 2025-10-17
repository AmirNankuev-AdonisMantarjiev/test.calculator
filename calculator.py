import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        self.display = tk.Entry(self.window, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '⌫'
        ]

        row = 1
        col = 0

        for button in buttons:
            if button == '=':
                cmd = self.calculate
                bg = 'orange'
            elif button == 'C':
                cmd = self.clear
                bg = 'red'
            elif button == '⌫':
                cmd = self.backspace
                bg = 'lightcoral'
            else:
                cmd = lambda x=button: self.add_to_display(x)
                bg = 'lightgray'

            tk.Button(
                self.window, text=button, font=('Arial', 15),
                command=cmd, bg=bg, height=2, width=5
            ).grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

    def add_to_display(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + value)

    def clear(self):
        self.display.delete(0, tk.END)

    def backspace(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Ошибка", "Некорректное выражение")
            self.clear()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

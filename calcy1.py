import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.memory = 0
        self.text_input = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+',
            '√', 'x^y', 'M+', 'MR'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.root, text=button, padx=20, pady=20, bd=8, fg="black", font=('arial', 20, 'bold'), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, button):
        if button == '=':
            try:
                total = str(eval(self.expression))
                self.text_input.set(total)
                self.expression = total
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.text_input.set("")
                self.expression = ""
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.text_input.set("")
                self.expression = ""
        elif button == 'C':
            self.text_input.set("")
            self.expression = ""
        elif button == '√':
            try:
                result = math.sqrt(eval(self.expression))
                self.text_input.set(str(result))
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid input for square root")
                self.text_input.set("")
                self.expression = ""
        elif button == 'x^y':
            self.expression += '**'
            self.text_input.set(self.expression)
        elif button == 'M+':
            try:
                self.memory = eval(self.expression)
                messagebox.showinfo("Memory", f"Stored {self.memory} in memory")
            except Exception:
                messagebox.showerror("Error", "Invalid input to store in memory")
        elif button == 'MR':
            self.text_input.set(str(self.memory))
            self.expression = str(self.memory)
        else:
            self.expression += str(button)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

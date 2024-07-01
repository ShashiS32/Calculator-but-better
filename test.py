import tkinter as tk
from tkinter import messagebox
import math

# Function to update the expression in the text entry box
def update_expression(number):
    current_text = expression.get()
    expression.set(current_text + str(number))

# Function to evaluate the final expression
def evaluate_expression():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear the text entry box
def clear_expression():
    expression.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# StringVar to store the expression
expression = tk.StringVar()

# Create the entry box
entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, column) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=evaluate_expression)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: update_expression(t))
    btn.grid(row=row, column=column)

# Add Clear button
btn_clear = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear_expression)
btn_clear.grid(row=4, column=2, columnspan=2)

# Run the main loop
root.mainloop()

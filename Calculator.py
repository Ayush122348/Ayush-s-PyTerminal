import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the calculator window
window = tk.Tk()
window.title("Calculator - By Ayush Kumar Kurrey")
window.config(bg="#E0E0E0")

# Create the input box
entry_style = ttk.Style()
entry_style.configure("TEntry", fieldbackground="#F0F0F0", borderwidth=0, font=("Arial", 20, "bold"), padding=10)
entry = ttk.Entry(window, style="TEntry")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="news")

# Create the number buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

button_style = ttk.Style()
button_style.configure("TButton", font=("Arial", 16, "bold"), padding=10, relief=tk.RAISED)

for button in buttons:
    text, row, col = button
    btn = ttk.Button(window, text=text, style="TButton", command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="news")

# Create the clear button
btn_clear = ttk.Button(window, text="C", style="TButton", command=button_clear)
btn_clear.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky="news")

# Create the equal button
btn_equal = ttk.Button(window, text="=", style="TButton", command=button_equal)
btn_equal.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="news")

# Configure row and column weights to expand with window
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Run the calculator
window.mainloop()

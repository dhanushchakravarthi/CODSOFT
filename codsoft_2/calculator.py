import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        output.config(text=f"Result: {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression\n{e}")

# Function to handle button clicks
def on_click(char):
    if char == '=':
        evaluate()
    else:
        entry.insert(tk.END, char)

# Create main application window
app = tk.Tk()
app.title("SmartCalc")
app.geometry("350x400")
app.config(bg="#1e1e2e")

# Input field for expressions
entry = tk.Entry(app, font=("Segoe UI", 20), bd=2, relief="groove", justify="right")
entry.pack(pady=20, padx=10, fill="x")

# Frame for buttons
buttons_frame = tk.Frame(app, bg="#1e1e2e")
buttons_frame.pack()

# Button layout
btns = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons dynamically
for row in btns:
    frame = tk.Frame(buttons_frame, bg="#1e1e2e")
    frame.pack()
    for char in row:
        b = tk.Button(frame, text=char, width=6, height=2, font=("Segoe UI", 16),
                      bg="#313244", fg="white", activebackground="#585b70",
                      command=lambda c=char: on_click(c))
        b.pack(side=tk.LEFT, padx=5, pady=5)

# Result display label
output = tk.Label(app, text="Result:", font=("Segoe UI", 16), bg="#1e1e2e", fg="#a6e3a1")
output.pack(pady=20)

# Start the main event loop
app.mainloop()

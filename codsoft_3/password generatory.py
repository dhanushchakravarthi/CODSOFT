import tkinter as tk
from tkinter import messagebox
import random
import string

def generate():
    length = length_scale.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    pw = result_entry.get()
    app.clipboard_clear()
    app.clipboard_append(pw)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

app = tk.Tk()
app.title("PassForge")
app.geometry("400x300")
app.config(bg="#0f172a")

title = tk.Label(app, text="Secure Password Generator", font=("Segoe UI", 16, "bold"), bg="#0f172a", fg="#facc15")
title.pack(pady=20)

length_scale = tk.Scale(app, from_=6, to=32, orient=tk.HORIZONTAL, label="Password Length",
                        font=("Segoe UI", 10), bg="#0f172a", fg="white", troughcolor="#334155")
length_scale.set(12)
length_scale.pack()

tk.Button(app, text="Generate", font=("Segoe UI", 12), command=generate,
          bg="#22d3ee", fg="#1e293b", width=15).pack(pady=10)

result_entry = tk.Entry(app, font=("Segoe UI", 12), justify="center")
result_entry.pack(pady=5)

tk.Button(app, text="Copy", font=("Segoe UI", 10), command=copy_password,
          bg="#4ade80", fg="black", width=10).pack(pady=5)

app.mainloop()

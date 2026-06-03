import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Enter valid password length")
        return

    length = int(length)

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

# Password Length
tk.Label(root, text="Password Length", font=("Arial", 12)).pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Generate Button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="lightgreen"
).pack(pady=10)

# Result Box
result_entry = tk.Entry(root, width=35, font=("Arial", 12))
result_entry.pack(pady=10)

# Copy Button
tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="lightblue"
).pack()

root.mainloop()
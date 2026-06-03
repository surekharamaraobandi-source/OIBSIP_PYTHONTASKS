import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter positive values")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal Weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

# Labels
tk.Label(root, text="Weight (kg)", font=("Arial", 12)).pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)", font=("Arial", 12)).pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Button
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="lightblue"
).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
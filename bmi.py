import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())
        height_m = height_cm / 100.0

        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 24.9 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create widgets
weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)
height_label = tk.Label(root, text="Height (cm):")
height_entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
result_label = tk.Label(root, text="")

# Grid layout
weight_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)
calculate_button.grid(row=2, columnspan=2)
result_label.grid(row=3, columnspan=2)

# Start the GUI event loop
root.mainloop()

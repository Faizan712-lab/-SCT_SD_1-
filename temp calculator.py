import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            messagebox.showinfo("No Conversion Needed", f"The temperature is the same in {to_unit}.")
            return

        conversions = {
            "Celsius": {
                "Fahrenheit": lambda c: (c * 9/5) + 32,
                "Kelvin": lambda c: c + 273.15,
            },
            "Fahrenheit": {
                "Celsius": lambda f: (f - 32) * 5/9,
                "Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
            },
            "Kelvin": {
                "Celsius": lambda k: k - 273.15,
                "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
            },
        }

        result = conversions[from_unit][to_unit](value)
        label_result.config(text=f"Result: {value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Temperature Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# Input frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_temp = tk.Label(frame_input, text="Temperature:")
label_temp.grid(row=0, column=0, padx=10, pady=5)
entry_temp = tk.Entry(frame_input, width=10)
entry_temp.grid(row=0, column=1, padx=10, pady=5)

# Unit selection
units = ["Celsius", "Fahrenheit", "Kelvin"]

label_from = tk.Label(frame_input, text="From:")
label_from.grid(row=1, column=0, padx=10, pady=5)
combo_from = ttk.Combobox(frame_input, values=units, state="readonly", width=10)
combo_from.grid(row=1, column=1, padx=10, pady=5)
combo_from.set("Celsius")

label_to = tk.Label(frame_input, text="To:")
label_to.grid(row=2, column=0, padx=10, pady=5)
combo_to = ttk.Combobox(frame_input, values=units, state="readonly", width=10)
combo_to.grid(row=2, column=1, padx=10, pady=5)
combo_to.set("Fahrenheit")

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Helvetica", 12))
label_result.pack(pady=10)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import ttk

def update_progress():
    new_value = progress_var.get()
    new_value += 10
    if new_value > 100:
        new_value = 0
    progress_var.set(new_value)
    progress_bar["value"] = new_value
    parent.after(1000, update_progress)  # Update every 1000 milliseconds (1 second)

parent = tk.Tk()
parent.title("Progress Bar Example")

# Create a Progress Bar widget
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(parent, variable=progress_var, maximum=100)
progress_bar.pack(padx=20, pady=20, fill="x")

parent.after(1000, update_progress)  # Start updating the progress bar
parent.mainloop()

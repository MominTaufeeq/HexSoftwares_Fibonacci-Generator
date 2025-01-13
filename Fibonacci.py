import tkinter as tk
from tkinter import messagebox


def generate_fibonacci():
    try:
        num_terms = int(entry.get())
        if num_terms <= 0:
            messagebox.showerror("Invalid Input", "Please enter greater number.")
            return

        fib_sequence = []
        a, b = 0, 1
        for _ in range(num_terms):
            fib_sequence.append(a)
            a, b = b, a + b

        result_label.config(
            text=f"Fibonacci Series: {', '.join(map(str, fib_sequence))}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")


# Initialize the GUI window
window = tk.Tk()
window.title("Fibonacci Series Generator")
window.geometry("400x300")

# Input label and entry
input_label = tk.Label(window, text="Enter the number of terms:")
input_label.pack(pady=10)

entry = tk.Entry(window, width=20)
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(window, text="Generate", command=generate_fibonacci)
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", wraplength=350, justify="left")
result_label.pack(pady=20)

# Run the GUI event loop
window.mainloop()

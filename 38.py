import tkinter as tk
from tkinter import messagebox

def rotate_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

def parse_matrix_input():
    input_text = input_textbox.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter a matrix.")
        return None

    lines = input_text.split("\n")
    matrix = []

    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        try:
            row = list(map(int, parts))
        except ValueError:
            messagebox.showerror("Invalid Input", f"Non-integer value found in row: {line}")
            return None
        matrix.append(row)

    # Ensure it's a square matrix
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        messagebox.showerror("Error", "Matrix must be square (e.g., 3x3, 4x4).")
        return None

    return matrix

def on_rotate():
    matrix = parse_matrix_input()
    if matrix is None:
        return

    rotated = rotate_matrix(matrix)
    output_textbox.config(state=tk.NORMAL)
    output_textbox.delete("1.0", tk.END)
    for row in rotated:
        output_textbox.insert(tk.END, " ".join(map(str, row)) + "\n")
    output_textbox.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Rotate Matrix 90° Clockwise")

tk.Label(root, text="Enter Square Matrix (space-separated rows):", font=("Arial", 12)).pack(pady=5)

input_textbox = tk.Text(root, height=8, width=40, font=("Consolas", 12))
input_textbox.pack()

tk.Button(root, text="Rotate 90° Clockwise", command=on_rotate, font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Rotated Matrix:", font=("Arial", 12)).pack(pady=5)

output_textbox = tk.Text(root, height=8, width=40, font=("Consolas", 12), state=tk.DISABLED)
output_textbox.pack()

root.mainloop()

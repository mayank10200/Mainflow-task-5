import tkinter as tk
from tkinter import messagebox

def is_valid_sudoku(board):
    def is_valid_block(block):
        nums = [x for x in block if x != '.' and x.isdigit()]
        return len(nums) == len(set(nums))

    for row in board:
        if not is_valid_block(row):
            return False

    for col in zip(*board):
        if not is_valid_block(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_block(block):
                return False

    return True

def validate():
    board = []
    try:
        for i in range(9):
            row = []
            for j in range(9):
                val = entries[i][j].get().strip()
                if val == "":
                    val = "."
                if val != "." and (not val.isdigit() or not (1 <= int(val) <= 9)):
                    raise ValueError(f"Invalid value at row {i+1}, column {j+1}: {val}")
                row.append(val)
            board.append(row)
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return

    if is_valid_sudoku(board):
        messagebox.showinfo("Sudoku Validator", "✅ This Sudoku board is VALID.")
    else:
        messagebox.showerror("Sudoku Validator", "❌ This Sudoku board is INVALID.")

# GUI setup
root = tk.Tk()
root.title("Sudoku Validator")

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=2, font=("Arial", 16), justify='center')
        entry.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(entry)
    entries.append(row_entries)

validate_button = tk.Button(root, text="Validate Sudoku", font=("Arial", 14), command=validate)
validate_button.grid(row=9, column=0, columnspan=9, pady=10)

root.mainloop()

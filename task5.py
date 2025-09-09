import tkinter as tk
from tkinter import ttk, messagebox
import random

class VirtualStockMarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Stock Market Simulator")
        self.root.geometry("500x600")
        self.stocks = {
            "AAPL": 100.0,
            "GOOG": 150.0,
            "TSLA": 200.0
        }
        self.portfolio = {}
        
        self.setup_ui()
        self.update_prices()

    def setup_ui(self):
        tk.Label(self.root, text="📊 Virtual Stock Market", font=("Arial", 16)).pack(pady=10)

        self.stock_frame = tk.Frame(self.root)
        self.stock_frame.pack(pady=10)

        self.price_labels = {}
        for stock in self.stocks:
            row = tk.Frame(self.stock_frame)
            row.pack(pady=2)
            lbl = tk.Label(row, text=f"{stock}: ₹{self.stocks[stock]:.2f}", font=("Arial", 12))
            lbl.pack()
            self.price_labels[stock] = lbl

        # Entry Frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Select Stock:").grid(row=0, column=0, sticky="e")
        self.stock_dropdown = ttk.Combobox(entry_frame, values=list(self.stocks.keys()), state="readonly")
        self.stock_dropdown.set("AAPL")  # Default
        self.stock_dropdown.grid(row=0, column=1)

        tk.Label(entry_frame, text="Quantity:").grid(row=1, column=0, sticky="e")
        self.qty_entry = tk.Entry(entry_frame)
        self.qty_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(self.root, text="Buy Stock", command=self.buy_stock, width=15).pack(pady=5)
        tk.Button(self.root, text="Sell Stock", command=self.sell_stock, width=15).pack(pady=5)
        tk.Button(self.root, text="View Portfolio", command=self.show_portfolio, width=15).pack(pady=5)

        self.portfolio_text = tk.Text(self.root, height=10, width=50, state='disabled', font=("Consolas", 10))
        self.portfolio_text.pack(pady=10)

        tk.Button(self.root, text="Refresh Prices", command=self.update_prices, width=20).pack(pady=10)

    def update_prices(self):
        for stock in self.stocks:
            change = random.uniform(-5, 5)
            self.stocks[stock] = round(self.stocks[stock] + change, 2)
            self.price_labels[stock].config(text=f"{stock}: ₹{self.stocks[stock]:.2f}")

    def buy_stock(self):
        stock = self.stock_dropdown.get()
        try:
            quantity = int(self.qty_entry.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a positive number")
            return

        price = self.stocks[stock]
        self.portfolio[stock] = self.portfolio.get(stock, 0) + quantity
        messagebox.showinfo("Success", f"✅ Bought {quantity} shares of {stock} at ₹{price:.2f}")

    def sell_stock(self):
        stock = self.stock_dropdown.get()
        try:
            quantity = int(self.qty_entry.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a positive number")
            return

        if self.portfolio.get(stock, 0) >= quantity:
            self.portfolio[stock] -= quantity
            messagebox.showinfo("Success", f"✅ Sold {quantity} shares of {stock} at ₹{self.stocks[stock]:.2f}")
        else:
            messagebox.showerror("Error", "❌ Not enough shares to sell")

    def show_portfolio(self):
        self.portfolio_text.config(state='normal')
        self.portfolio_text.delete("1.0", tk.END)

        if not self.portfolio:
            self.portfolio_text.insert(tk.END, "Portfolio is empty.\n")
        else:
            total_value = 0
            for stock, qty in self.portfolio.items():
                price = self.stocks[stock]
                value = price * qty
                total_value += value
                self.portfolio_text.insert(tk.END, f"{stock}: {qty} shares @ ₹{price:.2f} = ₹{value:.2f}\n")

            self.portfolio_text.insert(tk.END, f"\n💼 Total Portfolio Value: ₹{total_value:.2f}")

        self.portfolio_text.config(state='disabled')

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualStockMarketApp(root)
    root.mainloop()

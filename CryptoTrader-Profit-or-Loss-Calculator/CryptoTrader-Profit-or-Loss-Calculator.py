import tkinter as tk
from tkinter import messagebox

crypto_amount = []
total_buy = []

def handle_error(val):
    while True:
        try:
            return int(val)
        except ValueError:
            messagebox.showerror('Error', 'Enter a valid integer')

def take_input():
    count = 0
    while True:
        count += 1

        ns = handle_error(entry_ns.get())
        fee = handle_error(entry_fee.get())
        bp = handle_error(entry_bp.get())

        value = (ns + fee) / bp
        crypto_amount.append(value)
        total_buy.append(ns)

        if messagebox.askyesno('Another Transaction?', 'Do you want to add another transaction?'):
            entry_ns.delete(0, tk.END)
            entry_fee.delete(0, tk.END)
            entry_bp.delete(0, tk.END)
            continue
        break

    return sum(crypto_amount), sum(total_buy)

def trade():
    crypto_amount, total_buy = take_input()
    sp = handle_error(entry_sp.get())
    trade_value = (sp * crypto_amount) - total_buy
    messagebox.showinfo('Trade Result', f'Trade Value: {trade_value}')

# Create the main window
root = tk.Tk()
root.title("Crypto Trading")

# Create and place widgets
label_ns = tk.Label(root, text="Total Purchase in Naira:")
label_ns.pack()
entry_ns = tk.Entry(root)
entry_ns.pack()

label_fee = tk.Label(root, text="Charges:")
label_fee.pack()
entry_fee = tk.Entry(root)
entry_fee.pack()

label_bp = tk.Label(root, text="Unit Buying Price:")
label_bp.pack()
entry_bp = tk.Entry(root)
entry_bp.pack()

button_add_transaction = tk.Button(root, text="Add Transaction", command=take_input)
button_add_transaction.pack()

label_sp = tk.Label(root, text="Unit Selling Price:")
label_sp.pack()
entry_sp = tk.Entry(root)
entry_sp.pack()

button_trade = tk.Button(root, text="Trade", command=trade)
button_trade.pack()

# Run the main loop
root.mainloop()

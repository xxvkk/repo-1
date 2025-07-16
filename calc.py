import tkinter as tk
BG_COLOR = "#2E2E2E"      # Dark background
BTN_COLOR = "#3C3C3C"      # Button color
TEXT_COLOR = "white"       # Text color
OPERATOR_COLOR = "#FF006A" # Orange for operators
CLEAR_COLOR = "#FF3B30"    # Red for "C"
def add_to_display(symbol):
    entry.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка!")

def clear():
    entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("Калькулятор")
    root.geometry("300x400")

    global entry
    entry = tk.Entry(root, width=15, font=("Arial", 20), borderwidth=5, justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),bg=OPERATOR_COLOR,
            fg=TEXT_COLOR,
            activebackground="#FF00E6",  # Lighter orange on click
            command=calculate )
        elif text == "C":
            btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),bg=OPERATOR_COLOR,
            fg=TEXT_COLOR,
            activebackground="#E276BE", command=clear)
        else:
            btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: add_to_display(t))
        btn.grid(row=row, column=col, sticky="nsew")

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # Create the display widget
        self.display = tk.Entry(master, width=25, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Create the buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, command=lambda:self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        else:
            self.display.insert(tk.END, text)

# Create the main window
root = tk.Tk()

# Create the calculator instance
calculator = Calculator(root)

# Run the main loop
root.mainloop()

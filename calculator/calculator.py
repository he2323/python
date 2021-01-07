import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.formula = ''
        self.pack()
        self.create_widgets()

    def create_buttons(self):
        tk.Button(self.master, text="1", command=lambda: self.add_to_formula(1)).pack(side="left")
        tk.Button(self.master, text="2", command=lambda: self.add_to_formula(2)).pack(side="left")
        tk.Button(self.master, text="3", command=lambda: self.add_to_formula(3)).pack(side="left")
        tk.Button(self.master, text="4", command=lambda: self.add_to_formula(4)).pack(side="left")
        tk.Button(self.master, text="5", command=lambda: self.add_to_formula(5)).pack(side="left")
        tk.Button(self.master, text="6", command=lambda: self.add_to_formula(6)).pack(side="left")
        tk.Button(self.master, text="7", command=lambda: self.add_to_formula(7)).pack(side="left")
        tk.Button(self.master, text="8", command=lambda: self.add_to_formula(8)).pack(side="left")
        tk.Button(self.master, text="9", command=lambda: self.add_to_formula(9)).pack(side="left")
        tk.Button(self.master, text="+", command=lambda: self.add_to_formula("+")).pack(side="left")
        tk.Button(self.master, text="-", command=lambda: self.add_to_formula("-")).pack(side="left")
        tk.Button(self.master, text="/", command=lambda: self.add_to_formula("/")).pack(side="left")
        tk.Button(self.master, text="*", command=lambda: self.add_to_formula("*")).pack(side="left")

    def create_widgets(self):
        self.create_buttons()
        tk.Button(self.master, text="print formula", command=self.print_formula).pack(side="bottom")
        tk.Button(self.master, text="print result", command=self.print_result).pack(side="bottom")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def print_formula(self):
        print(self.formula)

    def print_result(self):
        print(eval(self.formula))

    def add_to_formula(self, value):
        self.formula += str(value)


root = tk.Tk()
app = Calculator(master=root)
app.mainloop()

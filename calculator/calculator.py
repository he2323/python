import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None, numbers={}):
        super().__init__(master)
        self.master = master
        self.numbers = numbers
        self.buttons = self.create_buttons()
        self.formula = 'formlua'
        self.pack()
        self.create_widgets()

    def create_buttons(self):
        buttons = []
        for name, value in self.numbers.items():
            print(value)
            buttons.append(tk.Button(self.master, text=name, command=lambda *args: self.add_to_formula(value)))
        return buttons

    def create_widgets(self):
        for button in self.buttons:
            button.pack(side="top")
        self.form = tk.Button(self.master, text="print formula", command=self.print_formula)
        self.form.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def print_formula(self):
        print(self.formula)

    def add_to_formula(self, value):
        print(value)
        self.formula = self.formula + str(value)


Numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
root = tk.Tk()
app = Calculator(master=root, numbers=Numbers)
app.mainloop()

import tkinter as tk


class ResultViewer(tk.Frame):

    def __init__(self, parent, results: dict, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.results = results

        self.title_one = tk.Label(text='Data Structure 1', font=('Elvetica', 16), background='#9AC5F4')
        self.title_one.grid(row=0, column=1, padx=50, pady=25)
        self.title_two = tk.Label(text='Data Structure 2', font=('Elvetica', 16), background='#9AC5F4')
        self.title_two.grid(row=0, column=2, padx=50, pady=25)

        for (key, value) in zip(results.keys(), results.values()):
            counter = 0


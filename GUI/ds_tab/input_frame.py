import tkinter as tk
from tkinter import scrolledtext


class InputFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        print(self.parent.__repr__())

        self.label_one = tk.Label(self, text='Data Structure 1', font=('Elvetica', 16))
        self.label_one.grid(row=0, column=0, padx=50, pady=25)
        self.box_one = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.box_one.grid(row=1, column=0, padx=50, pady=25)
        self.box_one.focus()

        self.label_two = tk.Label(self, text='Data Structure 2', font=('Elvetica', 16))
        self.label_two.grid(row=0, column=1, padx=50, pady=25)
        self.box_two = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.box_two.grid(row=1, column=1, padx=50, pady=25)

        self.match_button = tk.Button(
            self,
            text='Confronta',
            font=('Elvetica', 16),
            command=lambda: self.parent.find_differences(
                self.box_one.get('1.0', 'end-1c'),
                self.box_two.get('1.0', 'end-1c')
            ))
        self.match_button.grid(row=2, column=0, columnspan=2, padx=50, pady=25)

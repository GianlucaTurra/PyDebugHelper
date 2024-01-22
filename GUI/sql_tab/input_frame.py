import tkinter as tk
from tkinter import scrolledtext


class InputFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = tk.Label(self, text='Query sql da riformattare:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.input_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=177, height=35)
        self.input_box.grid(row=1, column=0, padx=50, pady=25)

        self.format_button = tk.Button(self,
                                       text='Formatta',
                                       command=lambda: self.parent.format_sql_string(
                                           self.input_box.get('1.0', 'end-1c')
                                       ),
                                       font=('Elvetica', 14))
        self.format_button.grid(row=2, column=0, padx=50, pady=15)

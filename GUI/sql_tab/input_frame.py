import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

from GUI.custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class InputFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Query sql da riformattare:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.input_box = CustomScrolledText(self, text_width=237, text_height=30)
        self.input_box.grid(row=1, column=0, padx=50, pady=25)

        self.format_button = ttk.Button(self,
                                        text='Formatta',
                                        command=lambda: self.parent.format_sql_string(
                                            self.input_box.get()
                                        ))
        self.format_button.grid(row=2, column=0, padx=50, pady=15)

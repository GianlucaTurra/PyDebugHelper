import tkinter as tk
from tkinter import ttk


class TextInput(ttk.Frame):

    def __init__(self, parent, label: str, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        if label.strip() != '':
            self.label = ttk.Label(self, text=label, font=('Elvetica', 12))
            self.label.grid(row=0, column=0, padx=10, pady=10)

        self.input_text = tk.StringVar()
        self.input = ttk.Entry(self, textvariable=self.input_text, font=('Elvetica', 12))
        self.input.grid(row=1, column=0, padx=10, pady=10)

    def get_input(self):
        return self.input_text.get()

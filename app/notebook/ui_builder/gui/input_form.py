import tkinter as tk
from tkinter import ttk


class InputForm(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.title = ttk.Label(self, text='Costruzione parametrizzata UI + Spaccati', font=('Elvetica', 16))
        self.title.grid(row=0, column=0, columnspan=2, padx=50, pady=25)



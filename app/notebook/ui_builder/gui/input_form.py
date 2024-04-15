import tkinter as tk
from tkinter import ttk

from custom_widgets.textinput.text_input import TextInput


class InputForm(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.title = ttk.Label(self, text='Costruzione parametrizzata UI + Spaccati', font=('Elvetica', 16))
        self.title.grid(row=0, column=0, columnspan=2, padx=50, pady=25)

        self.file_name = TextInput(self, 'Nome file fisico')
        self.file_name.grid(row=1, column=0, padx=15, pady=15)

        self.signature = TextInput(self, 'Sigla')
        self.signature.grid(row=1, column=1, padx=15, pady=15)

        self.galileo_pgm = TextInput(self, 'JG Pgm')
        self.galileo_pgm.grid(row=2, column=0, padx=15, pady=15)

        self.tracciato = TextInput(self, 'Tracciato record')
        self.tracciato.grid(row=2, column=1, padx=15, pady=15)

        self.work_item = TextInput(self, 'Work item')
        self.work_item.grid(row=3, column=0, padx=15, pady=15)

        self.create_files = ttk.Button(self, text='Crea files', command=lambda: self.call_creator())
        self.create_files.grid(row=4, column=0, columnspan=2, padx=15, pady=15)

    def call_creator(self):
        self.parent.create_files(
            self.file_name.get_input(),
            self.tracciato.get_input(),
            self.galileo_pgm.get_input(),
            self.signature.get_input(),
            self.work_item.get_input()
        )

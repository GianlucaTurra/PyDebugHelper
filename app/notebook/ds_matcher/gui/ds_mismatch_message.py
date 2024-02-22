import tkinter as tk
from tkinter import ttk
from typing import Dict


class MismatchMessage(tk.Toplevel):

    def __init__(self, parent, mismatching_keys: Dict, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title('Errore inserimento chiavi')

        self.error_message = ('Sono state trovate alcune differenze fra le chiavi delle DS, non è possibile eseguire '
                              'il confronto.')
        self.message = ttk.Label(self, text=self.error_message, foreground='red')
        self.message.grid(row=0, column=0, columnspan=2, padx=50, pady=25)

        self.block_one = Block(self, 'Presenti solo a sinistra', mismatching_keys['left'])
        self.block_one.grid(row=1, column=0)

        self.block_two = Block(self, 'Presenti solo a destra', mismatching_keys['right'])
        self.block_two.grid(row=1, column=1)


class Block(ttk.Frame):

    def __init__(self, parent, title, mismatching_keys, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title = ttk.Label(self, text=title, font=('Elvetica', 12))
        self.title.grid(row=0, column=0, padx=50, pady=25)

        self.row_counter = 1

        for key in mismatching_keys:
            self.mismatching_key = ttk.Entry(self)
            self.mismatching_key.insert(0, key)
            self.mismatching_key.configure(state='readonly')
            self.mismatching_key.grid(row=self.row_counter, column=0, padx=50, pady=5)
            self.row_counter += 1

import tkinter as tk
from tkinter import scrolledtext


class InsertDs(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.block_one = Block(self, 'Data Structure 1')
        self.block_one.grid(row=0, column=0)
        self.block_one.box.focus()
        self.block_two = Block(self, 'Data Structure 2')
        self.block_two.grid(row=0, column=1)
        self.button_block = ButtonBlock(self)
        self.button_block.grid(row=1, column=0, columnspan=2)


class Block(tk.Frame):

    def __init__(self, parent, text, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.label = tk.Label(self, text=text, font=('Elvetica', 16), background='#9AC5F4')
        self.label.grid(row=0, column=0, padx=50, pady=25)
        self.box = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.box.grid(row=1, column=0, padx=50, pady=25)


class ButtonBlock(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.match_button = tk.Button(
            self,
            text='Confronta',
            font=('Elvetica', 16),
            command=lambda: self.parent.parent.find_differences(
                self.parent.block_one.box.get('1.0', 'end-1c'),
                self.parent.block_two.box.get('1.0', 'end-1c')
            ))
        self.match_button.grid(row=0, column=0, padx=50, pady=25)

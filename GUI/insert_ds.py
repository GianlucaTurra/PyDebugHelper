import tkinter as tk
from tkinter import scrolledtext


class InsertDs(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.container_block = ContainerBlock(self)
        self.container_block.pack(side='top')
        self.button_block = ButtonBlock(self)
        self.button_block.pack(side='top')


class ContainerBlock(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.block_one = Block(self, 'Data Structure 1')
        self.block_one.pack(side='left')
        self.block_two = Block(self, 'Data Structure 2')
        self.block_two.pack(side='right')


class Block(tk.Frame):

    def __init__(self, parent, text, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.label = tk.Label(self, text=text, font=('Elvetica', 16), background='#9AC5F4')
        self.label.pack(side='top', padx=50, pady=25)
        self.box = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.box.pack(side='top', padx=50, pady=25)


class ButtonBlock(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='#9AC5F4')

        self.match_button = tk.Button(
            self,
            text='Confronta',
            font=('Elvetica', 16),
            command=lambda: placeholder(
                self.parent.container_block.block_one.box.get('1.0', 'end-1c'),
                self.parent.container_block.block_two.box.get('1.0', 'end-1c')
            ))
        self.match_button.pack(side='top', padx=50, pady=25)


def placeholder(str1: str, str2: str):
    x, y = str1, str2
    pass

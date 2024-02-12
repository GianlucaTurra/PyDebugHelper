import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk

import os


class CustomSearchBar(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.current_module_path = os.path.abspath(__file__)

        self.search_value = tk.StringVar()
        self.search_entry = ttk.Entry(self, textvariable=self.search_value)
        self.search_entry.grid(row=0, column=0)
        self.search_entry.bind('<Return>', lambda event: self.parent.search())

        self.icon_image = tk.PhotoImage(file=r'custom_widgets/searchbar/img/search_icon.png')
        self.icon = self.icon_image.subsample(38, 38)

        self.search_button = ttk.Button(
            self,
            image=self.icon,
            command=lambda: self.parent.search()
        )
        self.search_button.grid(row=0, column=1)

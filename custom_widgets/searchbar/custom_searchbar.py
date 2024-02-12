import sys

from PIL import Image, ImageTk

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

        self.icon_image = load_image(file_path='img/search_icon.png', subsample=38)

        self.search_button = ttk.Button(
            self,
            image=self.icon_image,
            command=lambda: self.parent.search()
        )
        self.search_button.grid(row=0, column=1)


def load_image(file_path, subsample=None):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    image_path = os.path.join(base_path, file_path)
    image = Image.open(image_path)
    if subsample:
        image = image.resize((image.width // subsample, image.height // subsample))
    return ImageTk.PhotoImage(image)

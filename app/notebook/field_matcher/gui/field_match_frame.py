import tkinter as tk
from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class FieldMatch(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent




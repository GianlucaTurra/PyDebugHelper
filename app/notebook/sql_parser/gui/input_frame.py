import tkinter as tk
from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class InputFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Query sql da riformattare:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.input_box = CustomScrolledText(self, text_width=157, text_height=25)
        self.input_box.grid(row=1, column=0, padx=50, pady=25)

        self.format_button = ttk.Button(self,
                                        text='Formatta',
                                        command=lambda: self.parent.format_sql_string(
                                            self.input_box.get(),
                                            self.all_caps.get()
                                        ))
        self.format_button.grid(row=2, column=0, padx=50, pady=15)

        self.all_caps = tk.BooleanVar()
        self.all_caps_checkbox = ttk.Checkbutton(
            self,
            text='Formatta in CAPS LOCK',
            variable=self.all_caps,
            onvalue=True,
            offvalue=False
        )
        self.all_caps_checkbox.grid(row=3, column=0, padx=50, pady=15)

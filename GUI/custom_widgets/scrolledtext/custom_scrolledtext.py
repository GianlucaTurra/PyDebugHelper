import tkinter as tk
from tkinter import ttk


class CustomScrolledText(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        style = ttk.Style()
        default_font = style.lookup("TLabel", "font")
        self.text_widget = tk.Text(self, wrap="none", width=237, height=30, font=default_font)
        self.text_widget.grid(row=0, column=0, sticky="nsew")

        self.y_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.text_widget.yview)
        self.y_scrollbar.grid(row=0, column=1, sticky="ns")
        self.x_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.text_widget.xview)
        self.x_scrollbar.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.text_widget.config(yscrollcommand=self.y_scrollbar.set, xscrollcommand=self.x_scrollbar.set)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def get(self) -> str:
        """
        Get the full content of the CustomScrolledText, like calling get(1.0, 'end-1c')
        from the tkinter Text widget or from tk.scrolledtext
        :return: Content of text as String
        """
        return self.text_widget.get(1.0, "end-1c")

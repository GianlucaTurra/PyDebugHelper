import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

from GUI.custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class OutputFrame(tk.Frame):

    def __init__(self, parent, formatted_string, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Query sql formattata:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        # self.output_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=177, height=35)
        # self.output_box.insert(tk.END, formatted_string)
        # self.output_box.configure(state='disabled')

        self.output_box = CustomScrolledText(self, text_width=237, text_height=30)
        self.output_box.grid(row=1, column=0, padx=50, pady=25)

        self.beck_to_insert = ttk.Button(self,
                                         text='Inserimento',
                                         command=lambda: self.parent.show_frame('input'))
        self.beck_to_insert.grid(row=2, column=0, padx=50, pady=15)

    def display_result(self, input_text: str) -> None:
        """
        Deletes existing text into the text box and replaces it with
        input_text
        :param input_text: Formatted SQL query
        :return: None
        """
        self.output_box.set_read_only_value(input_text)

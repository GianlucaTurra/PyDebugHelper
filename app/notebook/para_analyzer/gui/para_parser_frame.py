import tkinter as tk
from tkinter import ttk, messagebox

from app.notebook.ds_analyzer.modules.ds_matcher import get_funny_exclamation
from app.notebook.para_analyzer.modules.para_parsing import format_para, search_for_value
from custom_widgets.searchbar.custom_searchbar import CustomSearchBar


class ParaParser(ttk.Frame):

    def __init__(self, parent, input_frame, output_frame, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.input_frame = input_frame(self)
        self.input_frame.grid(row=0, column=0)

        self.output_frame = output_frame(self)
        self.output_frame.grid(row=0, column=1)

        self.parse_button = ttk.Button(self, text='Formatta', command=self.format_para)
        self.parse_button.grid(row=1, column=0, columnspan=2, padx=50, pady=25)

        self.search_bar = CustomSearchBar(self)
        self.search_bar.grid(row=2, column=0, columnspan=2, padx=50, pady=25)

        self.search_result = ttk.Entry(self, state='readonly', width=40)
        self.search_result.grid(row=3, column=0, columnspan=2, padx=50)

    def format_para(self) -> None:
        """
        Check if something is written inside the input text box.
        After the input is roughly validated the function to format the input string is called.
        Returned string from the parsing function is displayed in the output text box and set as
        read only.
        :return:
        """
        input_text = self.input_frame.get_input_text()
        if input_text is None:
            return
        output_text = format_para(input_text)
        self.output_frame.text_box.set_read_only_value(output_text)

    def search(self) -> None:
        """
        Reads input from the textbox and the SearchBar entry.
        The input text is mapped into a dictionary and the value retrieved using the
        entry as the key.
        :return:
        """
        search_text = self.search_bar.search_value.get().lower()
        if search_text.strip() == '':
            messagebox.showerror(
                'Nessuna chiave per la ricerca',
                f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!'
            )
            return
        input_text = self.input_frame.get_input_text().lower()
        if input_text.strip() == '':
            messagebox.showerror(
                'Nessun input',
                f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!'
            )
            return
        self.search_result.config(state='normal')
        self.search_result.delete(0, tk.END)
        self.search_result.insert(0, search_for_value(input_text, search_text))
        self.search_result.config(state='readonly')

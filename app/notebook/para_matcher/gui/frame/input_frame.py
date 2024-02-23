from tkinter import ttk, messagebox
import tkinter as tk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText
from custom_widgets.searchbar.custom_searchbar import CustomSearchBar
from app.notebook.para_matcher.modules.para_matcher import get_funny_exclamation, search_for_value


class ParaMatchInput(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.block_one = InputBlock(self, 'Parametro 1')
        self.block_one.grid(row=0, column=0)

        self.block_two = InputBlock(self, 'Parametro 2')
        self.block_two.grid(row=0, column=1)

        self.match_button = ttk.Button(
            self,
            text='Confronta',
            command=lambda: self.parent.find_differences(
                self.block_one.get_input_text(),
                self.block_two.get_input_text()
            )
        )
        self.match_button.grid(row=2, column=0, columnspan=2, padx=50, pady=25)


class InputBlock(ttk.Frame):

    def __init__(self, parent, title, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title = ttk.Label(self, text=title, font=('Elvetica', 16))
        self.title.grid(row=0, column=0, padx=50, pady=25)

        self.text_box = CustomScrolledText(self, text_width=72, text_height=25)
        self.text_box.grid(row=1, column=0, padx=50, pady=25)

        self.search_bar = CustomSearchBar(self)
        self.search_bar.grid(row=2, column=0, padx=50, pady=25)

        self.search_result = ttk.Entry(self, state='readonly', width=60)
        self.search_result.grid(row=3, column=0, padx=50)

    def get_input_text(self) -> str:
        """
        Method to return the input text of a block
        :return: Text in the box's input_box
        """
        return self.text_box.get()

    def search(self) -> None:
        """
        Method for the search_bar's command to search for a value for a specif key.
        Writes the value in the readonly entry
        :return:
        """
        search_text = self.search_bar.search_value.get().lower().strip()
        if search_text.strip() == '':
            messagebox.showerror(
                'Nessun parametro per la ricerca',
                f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!'
            )
            return
        input_text = self.text_box.get().lower().strip()
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

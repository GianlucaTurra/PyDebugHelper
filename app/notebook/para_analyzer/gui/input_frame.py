from tkinter import ttk
from tkinter import messagebox
from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText
from app.notebook.ds_analyzer.modules.ds_matcher import get_funny_exclamation


class InputFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Parametri da formattare', style='Title.TLabel')
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.text_box = CustomScrolledText(self, text_width=72, text_height=22)
        self.text_box.grid(row=1, column=0, padx=50, pady=25)

    def get_input_text(self) -> str | None:
        """
        Reads input text from the text box and checks if at least one character is written inside it.
        If nothing is written an error message is raised
        :return: The input text if it is provided; None if not.
        """
        input_text = self.text_box.get()
        if len(input_text.strip()) == 0:
            text = f'{get_funny_exclamation()} qualcuno si è dimenticato di scrivere qualcosa!'
            messagebox.showerror(title='Errore di inserimento', message=text)
            return
        return input_text

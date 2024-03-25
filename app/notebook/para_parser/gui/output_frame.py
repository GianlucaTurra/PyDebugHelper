from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class OutputFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Parametri formattati', style='Title.TLabel')
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.text_box = CustomScrolledText(self, text_width=72, text_height=20)
        self.text_box.grid(row=1, column=0, padx=50, pady=25)
        self.text_box.set_read_only_mode()

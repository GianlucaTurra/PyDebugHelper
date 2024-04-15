from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class OutputFrame(ttk.Frame):

    def __init__(self, parent, output_text: str, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.text_box = CustomScrolledText(self, text_width=90, text_height=35)
        self.text_box.grid()
        self.text_box.set_read_only_value(output_text)

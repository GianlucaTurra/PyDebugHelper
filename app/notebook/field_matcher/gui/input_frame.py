from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class InputFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.block_one = InputBlock(self, 'Tabella 1')
        self.block_one.grid(row=0, column=0)

        self.block_two = InputBlock(self, 'Tabella 2')
        self.block_one.grid(row=0, column=1)

        self.match_button = ttk.Button(self, text='Confronta', command=lambda: self.match_fields())
        self.match_button.grid(row=1, column=0, columnspan=2)

    def match_fields(self) -> None:
        pass


class InputBlock(ttk.Frame):
    def __init__(self, parent, label, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text=label)
        self.title_label.grid(row=0, column=0, padx=50, pady=15)

        self.input_box = CustomScrolledText(self)
        self.input_box.grid(row=1, column=0)

    def get_input_text(self) -> str:
        return self.input_box.get()

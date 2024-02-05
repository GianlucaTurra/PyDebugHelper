from tkinter import ttk

from GUI.custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class InputFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = ttk.Label(self, text='Parametri da formattare', style='Title.TLabel')
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.text_box = CustomScrolledText(self, text_width=105, text_height=25)
        self.text_box.grid(row=1, column=0, padx=50, pady=25)

from tkinter import ttk

from custom_widgets.scrolledtext.custom_scrolledtext import CustomScrolledText


class InputFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label_one = ttk.Label(self, text='Data Structure 1', font=('Elvetica', 16))
        self.label_one.grid(row=0, column=0, padx=50, pady=25)
        self.box_one = CustomScrolledText(self, text_width=105, text_height=25)
        self.box_one.grid(row=1, column=0, padx=50, pady=25)
        self.box_one.focus()

        self.label_two = ttk.Label(self, text='Data Structure 2', font=('Elvetica', 16))
        self.label_two.grid(row=0, column=1, padx=50, pady=25)
        self.box_two = CustomScrolledText(self, text_width=105, text_height=25)
        self.box_two.grid(row=1, column=1, padx=50, pady=25)

        self.match_button = ttk.Button(
            self,
            text='Confronta',
            command=lambda: self.parent.find_differences(
                self.box_one.get(),
                self.box_two.get()
            )
        )
        self.match_button.grid(row=2, column=0, columnspan=2, padx=50, pady=25)

import tkinter as tk
from tkinter import ttk


class CustomScrolledText(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, parent)
        self.parent = parent

        # TODO #1: Use a function from the proper module
        # TODO #2: Change font size and make it editable
        style = ttk.Style()
        style.configure('TLabel', font=('Elvetica', 12))
        default_font = style.lookup("TLabel", "font")
        self.text_widget = tk.Text(
            self,
            wrap="none",
            width=kwargs['text_width'],
            height=kwargs['text_height'],
            font=default_font
        )
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

    def clear(self) -> None:
        """
        Delete all the content of the Text widget
        :return:
        """
        self.text_widget.delete('1.0', tk.END)

    def set_read_only_mode(self) -> None:
        """
        Disable user input for the Text widget
        :return:
        """
        self.text_widget.configure(state='disabled')

    def set_editable_mode(self) -> None:
        """
        Enable user input for the Text widget
        :return:
        """
        self.text_widget.configure(state='normal')

    def set_read_only_value(self, input_text: str) -> None:
        """
        Insert value in the Text widget and disable user input
        :param input_text: String to insert into the widget
        :return:
        """
        self.set_editable_mode()
        self.clear()
        self.text_widget.insert(tk.END, input_text)
        self.set_read_only_mode()

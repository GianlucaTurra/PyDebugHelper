import tkinter as tk
from tkinter import ttk

from GUI.para_tab.modules.para_parsing import format_para
from GUI.para_tab.output_frame import OutputFrame
from GUI.para_tab.input_frame import InputFrame


class ParaParser(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.input_frame = InputFrame(self)
        self.input_frame.grid(row=0, column=0)

        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=0, column=1)

        self.parse_button = ttk.Button(self, text='Formatta', command=self.format_para)
        self.parse_button.grid(row=1, column=0, columnspan=2, padx=50, pady=25)

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

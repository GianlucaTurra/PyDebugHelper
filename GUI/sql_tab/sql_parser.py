import tkinter as tk
from tkinter import messagebox

from GUI.sql_tab.input_frame import InputFrame

import sqlparse

from GUI.sql_tab.output_frame import OutputFrame
from modules.ds_matcher import get_funny_exclamation

FRAMES = ['input', 'output']


class SqlParser(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.output_frame = OutputFrame(self, 'Niente da vedere qui')
        self.input_frame = InputFrame(self)
        self.input_frame.grid()

    def show_frame(self, frame_name: str) -> None:
        """
        Hides and shows frames based on input
        :param frame_name: frame to be shown
        :return: None
        """
        if frame_name == 'input':
            self.output_frame.grid_forget()
            self.input_frame.input_box.clear()
            self.input_frame.grid()
        if frame_name == 'output':
            self.input_frame.grid_forget()
            self.output_frame.grid()

    def format_sql_string(self, sql_string: str) -> None:
        """
        Checks if there's some kind of input text, if none is provided returns to input_frame
        The string is first reformatted to a single line to avoid unwanted behaviors in the following parsing
        Input string is formatted with SQL keywords turned into uppercase
        Output frame text box content is updated with the formatted string (cleaning previous text)
        Displays output frame and hides input frame
        :param sql_string: String received from input frame
        :return: None
        """
        if len(sql_string) == 0:
            text = f'{get_funny_exclamation()} qualcuno si è dimenticato di scrivere una query!'
            messagebox.showerror(title='Errore di inserimento', message=text)
            return
        sql_string = sql_string.replace('\n', '')
        formatted_sql_string = sqlparse.format(
            sql_string,
            reindent=True,
            keyword_case='upper',
            identifier_case='lower',
            use_space_around_operators=True,
            output_format='rpgle')
        self.output_frame.display_result(formatted_sql_string)
        self.show_frame('output')

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
        self.output_frame = None
        self.input_frame = InputFrame(self)
        self.input_frame.grid()

    def show_frame(self, frame_name: str) -> None:
        if frame_name == 'input':
            self.output_frame.grid_forget()
            self.input_frame.input_box.delete('1.0', tk.END)
            self.input_frame.grid()
        if frame_name == 'output':
            self.input_frame.grid_forget()
            self.output_frame.grid()

    def format_sql_string(self, sql_string: str) -> None:
        if len(sql_string) == 0:
            text = f'{get_funny_exclamation()} qualcuno si è dimenticato di scrivere una query!'
            messagebox.showerror(title='Errore di inserimento', message=text)
            return
        formatted_sql_string = sqlparse.format(sql_string, reindent=True, keyword_case='upper', identifier_case='lower',
                                               use_space_around_operators=True, output_format='rpgle') # , wrap_after=35
        self.output_frame = OutputFrame(self, formatted_sql_string)
        self.show_frame('output')

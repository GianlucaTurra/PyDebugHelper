import tkinter as tk
from tkinter import scrolledtext

import sqlparse

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


class InputFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = tk.Label(self, text='Query sql da riformattare:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.input_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=177, height=35)
        self.input_box.grid(row=1, column=0, padx=50, pady=25)

        self.format_button = tk.Button(self,
                                       text='Formatta',
                                       command=lambda: self.format_sql_string(
                                           self.input_box.get('1.0', 'end-1c')
                                       ),
                                       font=('Elvetica', 14))
        self.format_button.grid(row=2, column=0, padx=50, pady=15)

    def format_sql_string(self, sql_string: str) -> None:
        formatted_sql_string = sqlparse.format(sql_string, reindent=True, keyword_case='upper', identifier_case='lower')
        self.parent.output_frame = OutputFrame(self.parent, formatted_sql_string)
        self.parent.show_frame('output')


class OutputFrame(tk.Frame):

    def __init__(self, parent, formatted_string, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title_label = tk.Label(self, text='Query sql da riformattare:', font=('Elvetica', 16))
        self.title_label.grid(row=0, column=0, padx=50, pady=25)

        self.output_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=177, height=35)
        self.output_box.insert(tk.END, formatted_string)
        self.output_box.configure(state='disabled')
        self.output_box.grid(row=1, column=0, padx=50, pady=25)

        self.beck_to_insert = tk.Button(self,
                                        text='Inserimento',
                                        command=lambda: self.parent.show_frame('input'),
                                        font=('Elvetica', 14))
        self.beck_to_insert.grid(row=2, column=0, padx=50, pady=15)

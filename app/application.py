import tkinter as tk
from tkinter import ttk

from app.notebook.ds_analyzer.gui.ds_match_frame import DsMatchFrame
from app.notebook.ds_analyzer.gui.input_frame import InputFrame as DsInput
from app.notebook.ds_analyzer.gui.output_frame import OutputFrame as DsOutput
from app.notebook.para_analyzer.gui.para_parser_frame import ParaParser
from app.notebook.para_analyzer.gui.input_frame import InputFrame as ParaInput
from app.notebook.para_analyzer.gui.output_frame import OutputFrame as ParaOutput
from app.notebook.sql_parser.gui.sql_parser_frame import SqlParser
from app.notebook.sql_parser.gui.input_frame import InputFrame as SqlInput
from app.notebook.sql_parser.gui.output_frame import OutputFrame as SqlOutput


class App(tk.Tk):

    def __init__(self, notebook, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('Debug Utilities')
        self.state('zoomed')
        self.style = ttk.Style()
        self.notebook = notebook(self)
        self.frames = {
            'Controllo DS': DsMatchFrame(self.notebook, DsInput, DsOutput),
            'Sql parser': SqlParser(self.notebook, SqlInput, SqlOutput),
            'Para parser': ParaParser(self.notebook, ParaInput, ParaOutput)
        }
        self.notebook.add_frames(self.frames)
        self.default_style_configure()
        self.grid_configure()

    def default_style_configure(self) -> None:
        self.style.theme_use()
        self.style.configure(style='Title.TLabel', font=('Elvetica', 16))
        self.style.configure(style='Title.TFrame', background='#C7FFD8')
        self.style.configure(style='TButton', borderwidth=0)
        self.style.configure(style='TText', font=('Elvetica', 20))

    def grid_configure(self) -> None:
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.notebook.grid(sticky='nsew')

    def run(self) -> None:
        self.mainloop()

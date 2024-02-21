import tkinter as tk
from tkinter import ttk

from app.notebook.app_notebook import AppNoteBook
from app.notebook.ds_analyzer.gui.ds_match_frame import DsMatchFrame
from app.notebook.ds_analyzer.gui.input_frame import InputFrame as DsInput
from app.notebook.ds_analyzer.gui.output_frame import OutputFrame as DsOutput
from app.notebook.para_analyzer.gui.para_parser_frame import ParaParser
from app.notebook.para_analyzer.gui.input_frame import InputFrame as ParaInput
from app.notebook.para_analyzer.gui.output_frame import OutputFrame as ParaOutput
from app.notebook.sql_parser.gui.sql_parser_frame import SqlParser
from app.notebook.sql_parser.gui.input_frame import InputFrame as SqlInput
from app.notebook.sql_parser.gui.output_frame import OutputFrame as SqlOutput


def style_configure(app_style: ttk.Style) -> None:
    app_style.theme_use()
    app_style.configure('Title.TLabel', font=('Elvetica', 16))
    app_style.configure('Title.TFrame', background='#C7FFD8')
    app_style.configure('TButton', borderwidth=0)
    app_style.configure('TText', font=('Elvetica', 20))


class App(tk.Tk):

    def __init__(self, notebook, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('Debug Utilities')
        self.state('zoomed')
        self.style = ttk.Style()
        self.frames = {
            'Controllo DS': DsMatchFrame(notebook, DsInput, DsOutput),
            'Sql parser': SqlParser(notebook, SqlInput, SqlOutput),
            'Para parser': ParaParser(notebook, ParaInput, ParaOutput)
        }
        self.notebook = notebook(self)
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


# root = tk.Tk()
# root.title('Debug Utilities')
# root.state('zoomed')
# style = ttk.Style()
# style_configure(style)
# app = AppNoteBook(parent=root)
# frames = {
#     'Controllo DS': DsMatchFrame(app, DsInput, DsOutput),
#     'Sql parser': SqlParser(app, SqlInput, SqlOutput),
#     'Para parser': ParaParser(app, ParaInput, ParaOutput)
# }
# app.add_frames(frames)
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
# app.grid(sticky='nsew')
#
#
# def run_app():
#     app.mainloop()

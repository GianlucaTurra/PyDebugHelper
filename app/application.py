import tkinter as tk
from tkinter import ttk

from app.notebook.app_notebook import AppNoteBook
from app.notebook.ds_analyzer.gui.ds_match_frame import DsMatchFrame
from app.notebook.para_analyzer.gui.para_parser_frame import ParaParser
from app.notebook.sql_parser.gui.sql_parser_frame import SqlParser


def style_configure(style: ttk.Style) -> None:
    style.theme_use()
    style.configure('Title.TLabel', font=('Elvetica', 16))
    style.configure('Title.TFrame', background='#C7FFD8')
    # style.configure('TButton', foreground='#161D6F')
    # style.configure('TLabel', foreground='#98DED9', background='#F6F6F6')
    # style.configure('TFrame', background='#F6F6F6')


__frames = {'Controllo DS': DsMatchFrame, 'Sql parser': SqlParser, 'Para parser': ParaParser}
__root = tk.Tk()
__root.title('Debug Utilities')
__root.state('zoomed')
__style = ttk.Style()
style_configure(__style)
__app = AppNoteBook(parent=__root, frames=__frames)
__root.rowconfigure(0, weight=1)
__root.columnconfigure(0, weight=1)
__app.grid(sticky='nsew')


def run_app():
    __app.mainloop()

import tkinter as tk
from tkinter import ttk

from GUI.app_notebook import AppNoteBook
from GUI.ds_tab.ds_match import DsMatchFrame
from GUI.para_tab.para_parser import ParaParser
from GUI.sql_tab.sql_parser import SqlParser


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

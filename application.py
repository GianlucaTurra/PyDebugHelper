import tkinter as tk
from tkinter import ttk

from GUI.app_notebook import AppNoteBook
from GUI.ds_tab.ds_match import DsMatchFrame
from GUI.sql_tab.sql_parser import SqlParser

__frames = {'Controllo DS': DsMatchFrame, 'Sql parser': SqlParser}
__root = tk.Tk()
__root.title('Debug Utilities')
__root.state('zoomed')
__style = ttk.Style()
__style.theme_use()
__app = AppNoteBook(parent=__root, frames=__frames)
__app.grid()


def run_app():
    __app.mainloop()

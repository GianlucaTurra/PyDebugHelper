import tkinter as tk

from GUI.app_notebook import AppNoteBook
from GUI.insert_ds import InsertDs
from GUI.sql_parser import SqlParser

__root = tk.Tk()
__frames = {'Controllo DS': InsertDs, 'Sql parser': SqlParser}
__app = AppNoteBook(parent=__root, frames=__frames)
__app.grid()


def run_app():
    __app.mainloop()

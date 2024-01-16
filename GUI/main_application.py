import tkinter as tk
from tkinter import END

from modules.ds_matcher import match_multiple_ds, ds_to_dict

from GUI.result import ResultViewer
from GUI.notebook import NoteBook


class MainApplication(tk.Frame):

    def __init__(self, parent, frames, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.differences = {}
        self.parent.title('Custom Debug Utilities')
        self.notebook = NoteBook(self)

        for tab_name, frame in frames.items():
            self.notebook.add_frame(tab_name, frame)

        self.notebook.grid()

    def find_differences(self, ds_one: str, ds_two: str):
        ds_list = [ds_one, ds_two]
        ds_list = [ds_to_dict(ds) for ds in ds_list]
        self.differences = match_multiple_ds(ds_list)
        if self.differences is None:
            return
        # self.frame.grid_forget()
        # self.frame = ResultViewer(self, self.differences)
        # self.frame.grid()

    def show_insert(self):
        self.frame.grid_forget()
        self.frame = self.hidden_frame
        self.frame.block_one.box.delete('1.0', END)
        self.frame.block_two.box.delete('1.0', END)
        self.frame.grid()

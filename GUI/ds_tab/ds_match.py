import tkinter as tk

from GUI.ds_tab.output_frame import OutputFrame
from GUI.ds_tab.input_frame import InputFrame
from modules.ds_matcher import ds_to_dict, match_multiple_ds


class DsMatchFrame(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.frame = InputFrame(self)
        self.frame.grid(sticky='nsew')

    def find_differences(self, ds_one: str, ds_two: str) -> None:
        """
        Call to methods to find differences and initialize Output Frame
        populated with results
        :return: None
        """
        ds_list = [ds_one, ds_two]
        ds_list = [ds_to_dict(ds) for ds in ds_list]
        differences = match_multiple_ds(ds_list)
        if differences is None:
            return
        self.frame.grid_forget()
        self.frame = OutputFrame(self, differences)
        self.frame.place(in_=self, anchor='center', relx='.5', rely='.25')

    def show_insert(self) -> None:
        """
        Hides output frame to show the input frame
        :return: None
        """
        self.frame.place_forget()
        self.frame = InputFrame(self)
        self.frame.grid(sticky='nsew')

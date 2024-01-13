import tkinter as tk

from modules.ds_matcher import match_multiple_ds, ds_to_dict


class MainApplication(tk.Frame):

    def __init__(self, parent, frame, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.differences = {}
        self.parent.title('Data Structure Matcher')

        self.frame = frame(parent)
        self.frame.grid()

        def find_differences(ds_one: str, ds_two: str):
            ds_list = [ds_one, ds_two]
            ds_list = [ds_to_dict(ds) for ds in ds_list]
            self.differences = match_multiple_ds(ds_list)

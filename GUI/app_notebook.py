from tkinter import ttk


class AppNoteBook(ttk.Notebook):

    def __init__(self, parent, frames, *args, **kwargs):
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frames = {}

        for tab_name, frame in frames.items():
            self.add_frame(tab_name, frame)

    def add_frame(self, tab_name, frame):
        self.frames[tab_name] = frame
        self.add(frame(self), text=tab_name)

    def show_tab(self, tab_name):
        tab_index = list(self.frames.keys()).index(tab_name)
        self.select(tab_index)


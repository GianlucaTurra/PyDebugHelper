from tkinter import ttk


class NoteBook(ttk.Notebook):

    def __init__(self, parent, *args, **kwargs):
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frames = {}

    def add_frame(self, tab_name, frame):
        self.frames[tab_name] = frame
        self.add(frame(self), text=tab_name)

    def show_tab(self, tab_name):
        tab_index = list(self.frames.keys()).index(tab_name)
        self.select(tab_index)


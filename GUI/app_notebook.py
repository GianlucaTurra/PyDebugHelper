from tkinter import ttk, messagebox


class AppNoteBook(ttk.Notebook):

    def __init__(self, parent, frames, *args, **kwargs):
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.frames = {}

        for tab_name, frame in frames.items():
            self.add_frame(tab_name, frame)

        # TODO add a custom messagebox as tk.toplevel to show or not the tutorial
        # self.show_tutorial =

    def add_frame(self, tab_name: str, frame) -> None:
        """
        Adds frame to notebook creating a new tab
        :param tab_name: Name to be displayed
        :param frame: Content of a tab
        :return: None
        """
        self.frames[tab_name] = frame
        self.add(frame(self), text=tab_name)

    def show_tab(self, tab_name: str) -> None:
        """
        Automatically switch from tab to tab
        :param tab_name: Name of the tab to be displayed
        :return: None
        """
        tab_index = list(self.frames.keys()).index(tab_name)
        self.select(tab_index)


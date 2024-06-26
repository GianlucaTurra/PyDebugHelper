from tkinter import ttk


class OutputNoteBook(ttk.Notebook):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.frames = {}

    def add_frames(self, frames):
        for tab_name, frame in frames.items():
            self.add_frame(tab_name, frame)

    def add_frame(self, tab_name: str, frame) -> None:
        """
        Adds frame to notebook creating a new tab
        :param tab_name: Name to be displayed
        :param frame: Content of a tab
        :return: None
        """
        self.frames[tab_name] = frame
        self.add(frame, text=tab_name)

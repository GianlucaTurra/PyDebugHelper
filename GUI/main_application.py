import tkinter as tk


class MainApplication(tk.Frame):

    def __init__(self, parent, frame, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('Data Structure Matcher')

        self.frame = frame(parent)
        self.frame.pack()

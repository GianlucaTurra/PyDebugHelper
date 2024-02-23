from tkinter import ttk

from app.notebook.para_matcher.modules.para_matcher import para_to_dict, match_multiple_params


class ParaMatcher(ttk.Frame):

    def __init__(self, parent, input_frame, output_frame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frame = input_frame(self)
        self.frame.grid(sticky='nsew')
        self.output_frame = output_frame
        self.input_frame = input_frame

    def find_differences(self, para_one: str, para_two: str) -> None:
        """
        Call to methods to find differences and initialize Output Frame
        populated with results
        :return: None
        """
        params = [para_one, para_two]
        params = [para_to_dict(param) for param in params]
        differences = match_multiple_params(params, self.parent)
        if differences is None:
            return
        self.frame.grid_forget()
        self.frame = self.output_frame(self, differences)
        self.frame.place(in_=self, anchor='center', relx='.5', rely='.25')

    def show_insert(self) -> None:
        """
        Hides output frame to show the input frame
        :return: None
        """
        self.frame.place_forget()
        self.frame = self.input_frame(self)
        self.frame.grid(sticky='nsew')

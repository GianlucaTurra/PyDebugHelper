from tkinter import messagebox, ttk

from app.notebook.ds_matcher.modules.ds_matcher import get_funny_exclamation
from app.notebook.sql_parser.modules.sql_parser import parse_sql_string

FRAMES = ['input', 'output']


class SqlParser(ttk.Frame):

    def __init__(self, parent, input_frame, output_frame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.output_frame = output_frame(self)
        self.input_frame = input_frame(self)
        self.input_frame.grid()

    def show_frame(self, frame_name: str) -> None:
        """
        Hides and shows frames based on input
        :param frame_name: frame to be shown
        :return: None
        """
        if frame_name == 'input':
            self.output_frame.grid_forget()
            self.input_frame.input_box.clear()
            self.input_frame.grid()
        if frame_name == 'output':
            self.input_frame.grid_forget()
            self.output_frame.grid()

    def format_sql_string(self, sql_string: str, string_case: bool) -> None:
        """
        Checks if there's some kind of input text, if none is provided returns to input_frame
        The string is first reformatted to a single line to avoid unwanted behaviors in the following parsing
        Input string is formatted with SQL keywords turned into uppercase
        Output frame text box content is updated with the formatted string (cleaning previous text)
        By default the reserved keywords turn to uppercase while identifiers stay to lower. If the input's checkbutton
        is selected displays the query to caps lock (values inside strings aren't included)
        Displays output frame and hides input frame
        :param sql_string: String received from input frame's text box
        :param string_case: bool received from input frame's checkbutton
        :return: None
        """
        if len(sql_string.strip()) == 0:
            text = f'{get_funny_exclamation()} qualcuno si è dimenticato di scrivere una query!'
            messagebox.showerror(title='Errore di inserimento', message=text)
            return
        identifier_case = 'lower'
        if string_case:
            identifier_case = 'upper'
        sql_string = sql_string.replace('\n', '')
        formatted_sql_string = parse_sql_string(sql_string, identifier_case)
        self.output_frame.display_result(formatted_sql_string)
        self.show_frame('output')

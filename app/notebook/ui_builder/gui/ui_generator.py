from tkinter import ttk, messagebox

from app.notebook.ui_builder.gui.output_frame import OutputFrame
from app.notebook.ui_builder.modules.generate_ui import generate_ui_text


class UiGenerator(ttk.Frame):

    def __init__(self, parent, input_frame, output_notebook, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.input_frame = input_frame(self)
        self.input_frame.grid(row=0, column=0, padx=50, pady=15)

        self.output_notebook = output_notebook(self)
        self.output_notebook.grid(row=0, column=1, padx=50, pady=15)

        self.frames: dict = {}
        self.stop = False

    def create_files(self, file_name: str, tracciato: str, galileo_pgm: str, signature: str, work_item: str) -> None:
        self.stop = False
        self.validate_input(file_name, tracciato, galileo_pgm, signature, work_item)
        if self.stop:
            return
        ui_text = generate_ui_text(file_name, tracciato, galileo_pgm, signature, work_item)
        self.frames['UI'] = OutputFrame(self.output_notebook, ui_text)
        self.output_notebook.add_frames(self.frames)

    def validate_input(self, file_name: str, tracciato: str, galileo_pgm: str, signature: str, work_item: str) -> None:
        if file_name == '':
            answer = messagebox.askyesno(
                title='Nome File',
                message='Non è stato inserito un nome file, procedere ugualmente?'
            )
            if not answer:
                self.stop = True
                return
        if tracciato == '':
            answer = messagebox.askyesno(
                title='Nome Tracciato',
                message='Non è stato inserito un nome per il tracciato record, procedere ugualmente?'
            )
            if not answer:
                self.stop = True
                return
        if galileo_pgm == '':
            answer = messagebox.askyesno(
                title='Nome Programma',
                message='Non è stato inserito un nome per il programma in JGalileo, procedere ugualmente?'
            )
            if not answer:
                self.stop = True
                return
        if signature == '':
            answer = messagebox.askyesno(
                title='Sigla Programmatore',
                message='Non è stata inserita una sigla programmatore, procedere ugualmente?'
            )
            if not answer:
                self.stop = True
                return
        if work_item == '':
            answer = messagebox.askyesno(
                title='Work Item',
                message='Non è stato inserito un work item, procedere ugualmente?'
            )
            if not answer:
                self.stop = True
                return

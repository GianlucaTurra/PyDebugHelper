from app.notebook.ui_builder.modules.constants import *

from tkinter import messagebox


# TODO: add new error when input variables exceed the rpg max length constraints
# TODO: add new warning message for potential errors when input and constants length are mismatching


def substitute_file_name(line: str, file_name: str) -> str:
    if len(file_name) > len(FILE):
        messagebox.showwarning(title='Warning', message='La lunghezza del campo è superiore al placeholder.')
    if FILE in line:
        return line.replace(FILE, file_name)
    return line


def substitute_tracciato(line: str, tracciato: str) -> str:
    if len(tracciato) > len(TRACCIATO):
        pass
    if TRACCIATO in line:
        return line.replace(TRACCIATO, tracciato)
    return line


def substitute_galileo_pgm(line: str, galileo_pgm: str) -> str:
    if len(galileo_pgm) > len(JG_PGM):
        pass
    if JG_PGM in line:
        return line.replace(JG_PGM, galileo_pgm)
    return line


def substitute_signature(line: str, signature: str) -> str:
    if len(signature) > len(SIGLA):
        pass
    if SIGLA in line:
        return line.replace(SIGLA, signature)
    return line


def substitute_work_item(line: str, work_item: str) -> str:
    if len(work_item) > len(WORKITEM):
        pass
    if WORKITEM in line:
        return line.replace(WORKITEM, work_item)
    return line

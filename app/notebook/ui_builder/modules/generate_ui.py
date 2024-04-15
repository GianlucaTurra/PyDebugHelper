from app.notebook.ui_builder.modules.substitute_functions import *
from app.notebook.ui_builder.modules.input_validation import *

STANDARD_UI_TEMPLATE = 'app/notebook/ui_builder/modules/resources/standard_files/standard_ui.txt'


def generate_ui_text(file_name: str, tracciato: str, galileo_pgm: str, signature: str, work_item: str) -> str | None:
    output_text = ''
    if not validate_input(file_name, FILE, 'nome file'):
        return
    if not validate_input(tracciato, TRACCIATO, 'tracciato record'):
        return
    if not validate_input(galileo_pgm, JG_PGM, 'programma jgalileo'):
        return
    if not validate_input(signature, SIGLA, 'sigla programmatore'):
        return
    if not validate_input(work_item, WORKITEM, 'work item'):
        return
    with open(STANDARD_UI_TEMPLATE, 'r') as standard_ui:
        for line in standard_ui:
            line = substitute_file_name(line, file_name.upper())
            line = substitute_tracciato(line, tracciato.upper())
            line = substitute_galileo_pgm(line, galileo_pgm.upper())
            line = substitute_signature(line, signature.upper())
            line = substitute_work_item(line, work_item.upper())
            output_text += line
    return output_text

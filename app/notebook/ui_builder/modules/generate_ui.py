from app.notebook.ui_builder.modules.substitute_functions import *

STANDARD_UI_TEMPLATE = 'app/notebook/ui_builder/modules/resources/standard_files/standard_ui.txt'


def generate_ui_text(file_name: str, tracciato: str, galileo_pgm: str, signature: str, work_item: str) -> str:
    output_text = ''

    with open(STANDARD_UI_TEMPLATE, 'r') as standard_ui:
        for line in standard_ui:
            line = substitute_file_name(line, file_name.upper())
            line = substitute_tracciato(line, tracciato.upper())
            line = substitute_galileo_pgm(line, galileo_pgm.upper())
            line = substitute_signature(line, signature.upper())
            line = substitute_work_item(line, work_item.upper())
            output_text += line
    return output_text

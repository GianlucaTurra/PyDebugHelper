from tkinter import messagebox


def check_equal_length(input_text: str, placeholder: str) -> bool:
    if len(input_text) > len(placeholder):
        return False
    return True


def ask_to_proceed(field: str) -> bool:
    return messagebox.askyesno(
        title='Warning',
        message=f'La lunghezza del campo {field} non corrisponde al placeholder standard.\n'
                f'Potrebbe causare errori nel codice RPG.\n'
                f'Procedere ugualmente?'
    )


def validate_input(input_text: str, placeholder: str, field: str) -> False:
    if not check_equal_length(input_text, placeholder):
        if not ask_to_proceed(field):
            return False

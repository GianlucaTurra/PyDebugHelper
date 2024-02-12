from tkinter import messagebox


PARA_ERROR = 'Credo che il testo inserito abbia qualche problema.\nProbabilmente mancano le tag <.>/<,>'


def format_para(input_text: str) -> str | None:
    """
    Formats the IN_PARA or OUT_PARA to a string of key value pairs
    :param input_text: the PARA the user wrote in the input text box
    :return: the formatted string if the input is validated, None if not
    """
    if not check_tags(input_text):
        messagebox.showerror(title='Errore parametro', message=PARA_ERROR)
        return
    input_text = input_text.replace('\n', '').replace('<,>', '\n').replace('<.>', ' = ')
    return input_text


def check_tags(input_text: str) -> bool:
    """
    Checks if the string contains the tags used in the IN_PARA or OUT_PARA
    :param input_text: the PARA the user wrote in the input text box
    :return: True if both the tags are used at least one, False if not
    """
    if input_text.find('<.>') == -1:
        return False
    if input_text.find('<,>') == -1:
        return False
    return True


def para_to_dict(input_text: str) -> dict:
    key_value_pairs: list = input_text.replace('\n', '').replace('<,>', '\n').split('\n')
    key_value_pairs = [pair.split('<.>') for pair in key_value_pairs]
    para_dict = {}
    for pair in key_value_pairs[:-1]:
        para_dict[pair[0]] = pair[1]
    return para_dict


def search_for_value(input_text: str, search_value: str) -> str:
    para_dict = para_to_dict(input_text)
    return para_dict[search_value]

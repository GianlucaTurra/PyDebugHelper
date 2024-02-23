import random
from typing import Tuple, Set

from tkinter import messagebox

from app.notebook.para_matcher.gui.para_mismatch_message import MismatchMessage
from app.notebook.ds_matcher.modules.data_structures_controls import *


def get_funny_exclamation() -> str:
    """
    Randomly return a funny exclamation
    :return: Entry of the exclamations list
    """
    exclamations = ['Perdindirindina', 'Perdincibacco', 'Perbaccolina']
    return exclamations[random.randint(0, len(exclamations) - 1)]


def find_mismatching_keys(params: List[Dict[str, str]]) -> Tuple[Set, Set]:
    """
    Compares params keys to find mismatching ones
    :param params: Params with non-matching keys
    :return: Tuple of non-matching keys (only present in the first ds and only present in the second)
    """
    param_one_keys = set(params[0].keys())
    param_two_keys = set(params[1].keys())
    return (param_one_keys - param_two_keys), (param_two_keys - param_one_keys)


def show_para_composition_error(params: List[Dict], app) -> None:
    """
    Opens TopLevel window to show DS composition errors
    :param params: Two params to match
    :param app: Tk app to anchor the TopLevel Window
    :return: None
    """
    mismatching_keys = dict()
    mismatching_keys['left'] = find_mismatching_keys(params)[0]
    mismatching_keys['right'] = find_mismatching_keys(params)[1]
    MismatchMessage(app, mismatching_keys, 'Sono state trovate alcune differenze fra i parametri inseriti, '
                                           'non è possibile eseguire il confronto.')


def para_to_dict(input_text: str) -> dict:
    """
    Conversion function to return a dictionary from a given Palmax parameter list
    :param input_text: a P_PARM's value
    :return: Palmax P_PARM as a python dictionary
    """
    key_value_pairs: list = input_text.replace('\n', '').replace('<,>', '\n').split('\n')
    key_value_pairs = [pair.split('<.>') for pair in key_value_pairs]
    para_dict = {}
    for pair in key_value_pairs[:-1]:
        para_dict[pair[0]] = pair[1]
    return para_dict


def match_multiple_params(params: List[Dict], app) -> Dict[str, Tuple] | None:
    """
    If the data structures are not matching by length an askokcancel is raised
    If cancelled is pressed None will be return and further matching operations are aborted
    :param params: Two data structures to compare
    :param app: Passed to error function to display DS composition errors
    :return: Dictionary of entries with differences, values in a tuple
    """
    differences = {}
    if check_for_empty_input(params):
        messagebox.showerror(
            'Nessun input',
            f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!'
        )
        return
    if not check_for_equal_keys(params) or not check_for_equal_length(params):
        show_para_composition_error(params, app)
        return
    for (para_one, para_two) in zip(params[0].keys(), params[1].keys()):
        if params[0][para_one] != params[1][para_one]:
            differences[para_one] = (params[0][para_one], params[1][para_one])
    return differences


def search_for_value(input_text: str, search_text: str) -> str:
    """
    Returns the value of a given key after converting the input_text to a dictionary
    :param input_text: a single DS
    :param search_text: the key to search
    :return: searched key's value
    """
    try:
        para_dict = para_to_dict(input_text)
        return para_dict[search_text]
    except KeyError:
        messagebox.showerror(
            title='Parametro non trovato',
            message=f'Il parametro {search_text} non è presente nel testo in input!'
        )
        return ''

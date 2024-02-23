import random
from typing import Tuple, Set

from tkinter import messagebox

from app.notebook.ds_matcher.gui.ds_mismatch_message import MismatchMessage
from app.notebook.ds_matcher.modules.data_structures_controls import *


def get_funny_exclamation() -> str:
    """
    Randomly return a funny exclamation
    :return: Entry of the exclamations list
    """
    exclamations = ['Perdindirindina', 'Perdincibacco', 'Perbaccolina']
    return exclamations[random.randint(0, len(exclamations) - 1)]


def find_mismatching_keys(data_structures: List[Dict[str, str]]) -> Tuple[Set, Set]:
    """
    Compares data structures keys for non-matching keys
    :param data_structures: Data structures with non-matching keys
    :return: Tuple of non-matching keys (only present in the first ds and only present in the second)
    """
    ds_one_keys = set(data_structures[0].keys())
    ds_two_keys = set(data_structures[1].keys())
    return (ds_one_keys - ds_two_keys), (ds_two_keys - ds_one_keys)


def set_elements_message_printer(set_: set) -> str:
    """
    Creates a string to show in the messagebox
    :param set_: Set of differences between keys of data structures
    :return: String to desplay
    """
    output = ''
    for element in set_:
        output += f'{element}'
    return output


def show_ds_composition_error(data_structures: List[Dict], app) -> None:
    """
    Opens TopLevel window to show DS composition errors
    :param case: (deprecated)
    :param data_structures: Two data structures to match
    :param app: Tk app to anchor the TopLevel Window
    :return: None
    """
    mismatching_keys = dict()
    mismatching_keys['left'] = find_mismatching_keys(data_structures)[0]
    mismatching_keys['right'] = find_mismatching_keys(data_structures)[1]
    MismatchMessage(app, mismatching_keys, 'Sono state trovate alcune differenze fra le chiavi delle DS, '
                                           'non è possibile eseguire il confronto.')



def ds_to_dict(data_structure: str) -> dict:
    """
    Conversion of a data structure entry to a python dictionary
    :param data_structure:
    :return: Data structure as a dictionary
    """
    ds: dict = {}
    for line in data_structure.splitlines():
        entry = line.split('=')
        entry[0] = split_if_not_qualified(entry[0])
        if not check_if_value_is_num(entry[1].strip()):
            ds[entry[0].strip()] = entry[1].strip()[1:-1]
            continue
        if check_if_value_is_int(entry[1].strip()):
            ds[entry[0].strip()] = int(entry[1].strip()[:-1])
            continue
        ds[entry[0].strip()] = float(entry[1].strip())
    return ds


def match_multiple_ds(data_structures: List[Dict], app) -> Dict[str, Tuple] | None:
    """
    If the data structures are not matching by length an askokcancel is raised
    If cancelled is pressed None will be return and further matching operations are aborted
    :param data_structures: Two data structures to compare
    :param app: Passed to error function to display DS composition errors
    :return: Dictionary of entries with differences, values in a tuple
    """
    differences = {}
    if check_for_empty_input(data_structures):
        messagebox.showerror(
            'Nessun input',
            f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!'
        )
        return
    if not check_for_equal_keys(data_structures) or not check_for_equal_length(data_structures):
        show_ds_composition_error(data_structures, app)
        return
    for (ds1_key, ds2_key) in zip(data_structures[0].keys(), data_structures[1].keys()):
        if data_structures[0][ds1_key] != data_structures[1][ds1_key]:
            differences[ds1_key] = (data_structures[0][ds1_key], data_structures[1][ds1_key])
    return differences


def search_for_value(input_text: str, search_text: str) -> str:
    """
    Returns the value of a given key after converting the input_text to a dictionary
    :param input_text: a single DS
    :param search_text: the key to search
    :return: searched key's value
    """
    try:
        ds_dict = ds_to_dict(input_text)
        return ds_dict[search_text]
    except KeyError:
        messagebox.showerror(
            title='Chiave non trovata',
            message=f'La chiave {search_text} non è presente nel testo in input!'
        )
        return ''

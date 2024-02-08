import random
from typing import List, Dict, Tuple, Set

from tkinter import messagebox

from app.notebook.ds_analyzer.modules.data_structures_controls import split_if_not_qualified, check_if_value_is_num, check_if_value_is_int, \
    check_for_empty_input, check_for_equal_length, check_for_equal_keys


def get_funny_exclamation() -> str:
    """
    Randomly return a funny exclamation
    :return: Entry of the exclamations list
    """
    exclamations = ['Perdindirindina', 'Perdincibacco', 'Perbaccolina']
    return exclamations[random.randint(0, len(exclamations) - 1)]


def find_not_matching_keys(data_structures: List[Dict[str, str]]) -> Tuple[Set, Set]:
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


def show_ds_composition_error(case: str, data_structures: List[Dict]) -> None:
    """
    Given an error case a different error message will be displayed
    """
    text = ''
    if case == 'length mismatch':
        text = 'La lunghezza delle due DS non combacia.'
    elif case == 'keys mismatch':
        text = 'Le chiavi delle due DS non combaciano.'
    left_diff = set_elements_message_printer(find_not_matching_keys(data_structures)[0])
    right_diff = set_elements_message_printer(find_not_matching_keys(data_structures)[1])
    message = (f'{text}\n'
               f'Presenti solo a sinistra: {left_diff}\n'
               f'Presenti solo a destra: {right_diff}')
    messagebox.showerror(title='Strutture dati non corrispondenti', message=message)


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


def match_multiple_ds(data_structures: List[Dict]) -> Dict[str, Tuple] | None:
    """
    If the data structures are not matching by length an askokcancel is raised
    If cancelled is pressed None will be return and further matching operations are aborted
    :param data_structures: Two data structures to compare
    :return: Dictionary of entries with differences, values in a tuple
    """
    differences = {}
    if check_for_empty_input(data_structures):
        messagebox.showerror(
            'Nessun input',
            f'{get_funny_exclamation()} sembra che qualcuno si sia dimenticato di scrivere qualcosa!')
        return
    if not check_for_equal_length(data_structures):
        show_ds_composition_error('length mismatch', data_structures)
        return
    if not check_for_equal_keys(data_structures):
        show_ds_composition_error('keys mismatch', data_structures)
        return
    for (ds1_key, ds2_key) in zip(data_structures[0].keys(), data_structures[1].keys()):
        if data_structures[0][ds1_key] != data_structures[1][ds1_key]:
            differences[ds1_key] = (data_structures[0][ds1_key], data_structures[1][ds1_key])
    return differences

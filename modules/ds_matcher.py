from typing import List, Dict, Tuple, Set

from tkinter import messagebox


def check_for_num(entry_value: str) -> bool:
    """
    :param entry_value: Value of the dictionary entry
    :return: True if the value is a number
    """
    try:
        float(entry_value)
    except ValueError:
        return False
    return True


def check_for_int(entry_value: str) -> bool:
    """
    A number value ending with '.' is and int
    :param entry_value: Value of the dictionary entry
    :return: True if the value is and int
    """
    if entry_value[-1] == '.':
        return True
    return False


def check_for_non_qualified(entry_key: str) -> str:
    """
    For nonqualified ds the key has to be split
    :param entry_key: Ds entry key
    :return: New key value
    """
    return entry_key.split(' OF ')[0]


def check_ds_length(data_structures: List[Dict]) -> bool:
    if len(data_structures[0]) == len(data_structures[1]):
        return True
    return False


def find_not_matching_keys(data_structures: List[Dict[str, str]]) -> Tuple[Set, Set]:
    ds_one_keys = set(data_structures[0].keys())
    ds_two_keys = set(data_structures[1].keys())
    return (ds_one_keys - ds_two_keys), (ds_two_keys - ds_one_keys)


def set_elements_message_printer(set_: set) -> str:
    """

    :param set_:
    :return:
    """
    output = ''
    for element in set_:
        output += f'{element}'
    return output


def ds_to_dict(data_structure: str) -> dict:
    """
    Conversion of a data structure entry to a python dictionary
    :param data_structure:
    :return: Data structure as a dictionary
    """
    ds: dict = {}
    for line in data_structure.splitlines():
        entry = line.split('=')
        entry[0] = check_for_non_qualified(entry[0])
        if not check_for_num(entry[1].strip()):
            ds[entry[0].strip()] = entry[1].strip()[1:-1]
            continue
        if check_for_int(entry[1].strip()):
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
    if not check_ds_length(data_structures):
        left_diff = set_elements_message_printer(find_not_matching_keys(data_structures)[0])
        right_diff = set_elements_message_printer(find_not_matching_keys(data_structures)[1])
        message = (f'La lunghezza delle due DS non combacia.\n'
                   f'Presenti solo a sinistra: {left_diff}\n'
                   f'Presenti solo a destra: {right_diff}')
        messagebox.showerror(title='Strutture dati non corrispondenti', message=message)
        return
    for (ds1_key, ds2_key) in zip(data_structures[0].keys(), data_structures[1].keys()):
        if data_structures[0][ds1_key] != data_structures[1][ds1_key]:
            differences[ds1_key] = (data_structures[0][ds1_key], data_structures[1][ds1_key])
    return differences

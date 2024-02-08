from typing import List, Dict


def check_if_value_is_num(entry_value: str) -> bool:
    """
    :param entry_value: Value of the dictionary entry
    :return: True if the value is a number
    """
    try:
        float(entry_value)
    except ValueError:
        return False
    return True


def check_if_value_is_int(entry_value: str) -> bool:
    """
    A number value ending with '.' is and int
    :param entry_value: Value of the dictionary entry
    :return: True if the value is and int
    """
    if entry_value[-1] == '.':
        return True
    return False


def split_if_not_qualified(entry_key: str) -> str:
    """
    For nonqualified ds the key has to be split
    :param entry_key: Ds entry key
    :return: New key value
    """
    return entry_key.split(' OF ')[0]


def check_for_equal_length(data_structures: List[Dict]) -> bool:
    """
    :param data_structures:
    :return: True if the lengths are equals
    """
    if len(data_structures[0]) == len(data_structures[1]):
        return True
    return False


def check_for_equal_keys(data_structures: List[Dict]) -> bool:
    """
    :param data_structures:
    :return: True if the keys are matching
    """
    if data_structures[0].keys() == data_structures[1].keys():
        return True
    return False


def check_for_empty_input(data_structures: List[Dict]) -> bool:
    """
    :param data_structures:
    :return:
    """
    if len(data_structures[0]) == 0 and len(data_structures[1]) == 0:
        return True
    return False

from typing import List, Dict


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

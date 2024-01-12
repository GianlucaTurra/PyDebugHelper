from typing import List, Dict, Tuple


def check_for_num(entry_value: str) -> bool:
    try:
        float(entry_value)
    except Exception as e:
        return False
    return True


def ds_to_dict(data_structure: str) -> dict:
    ds: dict = {}
    for line in data_structure.splitlines():
        entry = line.split('=')
        if check_for_num(entry[1].strip()):
            ds[entry[0].strip()] = float(entry[1].strip())
        else:
            ds[entry[0].strip()] = entry[1].strip()[1:-1]
    return ds


def match_multiple_ds(data_structures: List[Dict]) -> dict:
    differences = {}
    for (ds1_key, ds2_key) in zip(data_structures[0].keys(), data_structures[1].keys()):
        if data_structures[0][ds1_key] != data_structures[1][ds1_key]:
            differences[ds1_key] = (data_structures[0][ds1_key], data_structures[1][ds1_key])
    return differences

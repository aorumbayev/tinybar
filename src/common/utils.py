from os.path import exists
from typing import List
from src.common.models import ASA
import json


def load_tinybar_data(path: str):
    """
    Loads TinyBar data from a file. Returns None if file not exists.
    """
    if exists(path):
        with open(path, "r") as f:
            return [ASA(**asa_dict) for asa_dict in json.load(f)]
    else:
        return None


def save_tinybar_data(path: str, asas: List[ASA]):
    """
    Save TinyBar data into a file.
    """
    with open(path, "w") as f:
        json.dump([asa.dict() for asa in asas], f)

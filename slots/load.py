import json
import logging
import os

import numpy as np

from .key import keys

inverted_keys = {key: value for (value, key) in keys.items()}


def convert_data(data):
    board = []

    for y, row in enumerate(data):
        board.append([])
        for x, i in enumerate(row):
            # save key
            if isinstance(i, list):
                new = inverted_keys[i[0]](x, y, inverted_keys[i[1]])
            else:
                new = inverted_keys[i](x, y)
            board[-1].append(new)
    return np.array(board)


def load_path(path: str):
    if not os.path.exists(path):
        logging.warning(f"invalid board path {path}")
        return "empty"

    # get save
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        try:
            data = convert_data(data)
            logging.info("save loaded")
        except IndexError:
            logging.warning("save loaded but conversion failed - using empty board")
            return "empty"
    return data


def load_slot(slot: int):
    # check for valid slot id
    if type(slot) != int or slot < 0 or slot > 9:
        logging.warning(f"invalid slot when trying to load save {slot=}")
        return "empty"

    # check for empty save
    file_name = f"./saves/slot_{slot}/board.json"
    if not os.path.exists(file_name):
        logging.info("loaded empty save")
        return "empty"

    # get save
    return load_path(file_name)

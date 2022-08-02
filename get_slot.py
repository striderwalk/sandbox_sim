import os
import logging
import pickle


def get_saved():
    for i in range(10):
        if os.path.exists(f"./saves/slot_{i}/board.pickle"):
            yield True
        else:
            yield False


def load_slot(slot: int):
    if type(slot) != int or 0 > slot or slot > 9:
        logging.warning(f"invalid slot when trying to load save {slot=}")
        return None

    file_name = f"./saves/slot_{slot}/board.pickle"
    if not os.path.exists(file_name):
        logging.info("loaded empty save")
        return "empty"
    with open(file_name, "rb") as file:
        data = pickle.load(file)
        logging.info("loaded save")

    return data


def save_slot(board, slot):
    if type(slot) != int or 0 > slot or slot > 9:
        logging.warning("invalid save slot when trying to save save")
        return None

    file_name = f"./saves/slot_{slot}/board.pickle"
    if not os.path.exists(file_name):
        setup()

    with open(file_name, "wb") as f:
        logging.info(f"save board to slot {slot}")
        pickle.dump(board.board, f, pickle.HIGHEST_PROTOCOL)

def setup():
    if not os.path.exists("./saves"):
        os.mkdir("./saves")

    for i in range(10):
        if not os.path.exists(f"./saves/slot_{i}"):
            os.mkdir(f"./saves/slot_{i}")


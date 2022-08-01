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
    if type(slot) != int or 1 > slot or slot > 9:
        logging.warning("invalid slot when trying to load save")
        return None

    slotname = f"./saves/slot_{slot}"
    if not os.path.exists(slotname):
        logging.info("save slot does not exist")
        return "Fail"
    with open(slotname + "/board.pickle", "rb") as file:
        data = pickle.load(file)

    return data


def save_slot(board, slot):
    if type(slot) != int or 1 > slot or slot > 9:
        logging.warning("invalid save slot when trying to save save")
        return None

    slotname = f"./saves/slot_{slot}"
    if not os.path.exists(slotname):
        logging.INFO("save slot does not exist")
        return "Fail"

    with open("data", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

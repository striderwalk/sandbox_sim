import os
import logging


def get_empty():
    # return index of first empty slot
    for i in range(10):
        if not os.path.exists(f"./saves/slot_{i}/board.json"):
            return i


def get_saved():
    # return image of board if slot has been saved
    # if not return imgage if cross
    for i in range(10):
        if os.path.exists(f"./saves/slot_{i}/board.json"):
            ## allow for slot with no img but board for debug / dev
            if os.path.exists(f"./saves/slot_{i}/board.png"):
                yield f"./saves/slot_{i}/board.png"
            else: yield "./assets/empty.png"
        else:
            yield "./assets/cross.png"


def setup():
    # check saves folder
    if not os.path.exists("./saves"):
        logging.info("save folder not found - making one")
        os.mkdir("./saves")

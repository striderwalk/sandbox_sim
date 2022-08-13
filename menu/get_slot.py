import os
import logging
import pickle
import pygame


def get_saved():
    # return image of board or cross
    for i in range(10):
        if os.path.exists(f"./saves/slot_{i}/board.png"):
            yield f"./saves/slot_{i}/board.png"
        else:
            yield "./assets/cross.png"


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


def save_slot(board, slot, img):
    if type(slot) != int or 0 > slot or slot > 9:
        logging.warning("invalid save slot when trying to save save")
        return None
    file_name = f"./saves/slot_{slot}"
    board_name = file_name + "/board.pickle"
    image_name = file_name + "/board.png"
    print(board_name)
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    with open(board_name, "wb") as f:
        logging.info(f"save board to slot {slot}")
        pickle.dump(board.board, f, pickle.HIGHEST_PROTOCOL)
    pygame.image.save(img, image_name)


def setup():
    if not os.path.exists("./saves"):
        os.mkdir("./saves")



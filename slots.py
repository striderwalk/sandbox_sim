import os
import logging
import pickle
import pygame
import numpy as np


def get_empty():
    # return index of first empty slot
    for i in range(10):
        if not os.path.exists(f"./saves/slot_{i}/board.pickle"):
            return i


def get_saved():
    # return image of board if slot has been saved
    # if not return imgage if cross
    for i in range(10):
        if os.path.exists(f"./saves/slot_{i}/board.png"):
            yield f"./saves/slot_{i}/board.png"
        else:
            yield "./assets/cross.png"


def load_path(path: str):
    if not os.path.exists(path):
        logging.warning(f"invalid board path {path}")
        return "empty"

    # get save
    with open(path, "rb") as file:
        data = pickle.load(file)
        logging.info("loaded save")

    return data


def load_slot(slot: int):
    # check for vaild slot id
    if type(slot) != int or slot < 0 or slot > 9:
        logging.warning(f"invalid slot when trying to load save {slot=}")
        return None
    # check for empty save
    file_name = f"./saves/slot_{slot}/board.pickle"
    if not os.path.exists(file_name):
        logging.info("loaded empty save")
        return "empty"
    # get save
    with open(file_name, "rb") as file:
        data = pickle.load(file)
        logging.info("loaded save")
    return data


def save_slot(board, slot, img):
    # check for vaild slot id
    if type(slot) != int or 0 > slot or slot > 9:
        logging.warning("invalid save slot when trying to save save")
        return None
    file_name = f"./saves/slot_{slot}"
    board_name = file_name + "/board.pickle"
    image_name = file_name + "/board.png"
    # check for slot file
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    # save slot
    with open(board_name, "wb") as f:
        logging.info(f"save board to slot {slot}")
        pickle.dump(board.board, f, pickle.HIGHEST_PROTOCOL)
    pygame.image.save(img, image_name)

    if np.array_equal(board.board, load_slot(slot)):
        raise ValueError


def setup():
    # check saves folder
    if not os.path.exists("./saves"):
        os.mkdir("./saves")

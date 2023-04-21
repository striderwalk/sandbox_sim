import json
import logging
import os

import pygame

from .key import keys


def convert_board(board):
    data = []

    for row in board.board:
        data.append([])
        for i in row:
            # save key
            if not type(i).__name__ == "Fountain":
                new = keys[type(i)]
            else:
                new = [keys[type(i)], keys[i.obj]]

            data[-1].append(new)

    return data


def save_slot(board, slot, img):
    # check for vaild slot id
    if type(slot) != int or 0 > slot or slot > 9:
        logging.warning("invalid save slot when trying to save save")
        return None

    folder_name = f"./saves/slot_{slot}"
    board_name = folder_name + "/board.json"
    image_name = folder_name + "/board.png"
    # check for slot file
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    try:
        save_data = convert_board(board)
    except IndexError:
        logging.critical("board convertion failed board data lost")

    # save slot
    with open(board_name, "w", encoding="UTF-8") as file:
        json.dump(save_data, file)

        logging.info(f"save board to slot {slot}")

    pygame.image.save(img, image_name)

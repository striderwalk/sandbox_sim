import logging

import pygame
from conts import CELL_HEIGHT, HEIGHT, LOWER_BOARDER, UPPER_BOARDER, WIDTH
from sandbox_game.mouse import Mouse
from sandbox_game.selection import Selection
import errors
import settings

from .game_menu import Menu


class Game:
    """
    class to handle game menus/settings
    """

    def __init__(self, size, index, slot=0):
        self.save_slot = slot
        self.menu = Menu()
        self.menu.add_button("menu", ("=", "=", settings.sim_running), default=True)
        self.menu.add_button("pause", ("pause", "play", settings.pause))
        self.menu.add_button("temp", ("show temp", "show normal", settings.showtemp))
        self.mouse = Mouse(size)
        self.selection = Selection(index)
        self.pause_time = 0

    @property
    def shown(self):
        logging.warning("use settings.showmenu instead of this.")
        return settings.showmenu

    def update(self, win, board):
        if settings.pause.value:
            self.pause_time += 1

        # draw particle selection
        surf = pygame.Surface((WIDTH, HEIGHT - LOWER_BOARDER))
        self.selection.update(surf)
        win.blit(surf, (0, LOWER_BOARDER + CELL_HEIGHT))

        # draw menu
        surf = pygame.Surface((WIDTH, UPPER_BOARDER))
        self.menu.draw(surf)
        win.blit(surf, (0, 0))

        _clicks = self.mouse.update(win, board.board, self.selection.selected)
        return _clicks

    def handle_event(self, event):

        if event["handler"] == "selection":
            self.selection.handle_event(event)
        else:
            raise errors.EventNotHandled(event)

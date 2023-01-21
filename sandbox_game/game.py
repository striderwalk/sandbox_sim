import logging
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
        self.menu.add_button("pause", ("pause", "play", settings.pause))
        self.menu.add_button("temp", ("show temp", "show normal", settings.showtemp))
        self.mouse = Mouse(size)
        self.selection = Selection(index)

    @property
    def shown(self):
        logging.warning("use settings.showmenu instead of this.")
        return settings.showmenu

    def update(self, win, board):
        self.selection.update(win)
        self.menu.draw(win)

        _events = self.mouse.update(
            win, board.board, self.selection.selected, settings.showmenu.value
        )
        return _events

    def handle_event(self, event):
        if event["handler"] == "selection":
            self.selection.handle_event(event)
        else:
            raise errors.EventNotHandled(event)

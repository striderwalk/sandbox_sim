from .game_menu import Menu
import settings
import errors


class Game:
    """
    class to handle game menus/settings
    """

    def __init__(self, slot=0, pause=False, show_temp=False):
        self.save_slot = slot
        self.menu = Menu()
        self.menu.add_button("pause", ("pause", "play", settings.pause))
        self.menu.add_button("temp", ("show temp", "show normal", settings.showtemp))

    @property
    def shown(self):
        logging.warning("use settings.showmenu instead of this.")
        return settings.showmenu

    def draw_menu(self, win):
        self.menu.draw(win)

    def handle(self, event):
        if event["type"] == "toggle_play":  # pause game
            settings.toggle_pause()

        elif event["type"] == "temp":
            settings.toggle_showtemp()

        else:
            raise errors.EventNotHandled(event)

from .game_menu import Menu


class Game:
    """
    class to handle game menus/settings
    """

    def __init__(self, slot=0, pause=False, show_temp=False):
        self.save_slot = slot
        self.pause = pause
        self.show_temp = show_temp
        self.menu = Menu()
        self.menu.add_button("pause", ("pause", "play", self.toggle_pause))
        self.menu.add_button(
            "temp", ("show temp", "show normal", self.toggle_show_temp)
        )

    @property
    def shown(self):
        return not self.menu.menu_button.clicked

    def toggle_pause(self):
        self.pause = not self.pause
        self.menu.toggle("pause")

    def toggle_show_temp(self):
        self.show_temp = not self.show_temp
        self.menu.toggle("temp")

    def draw_menu(self, win):
        self.menu.draw(win)

    def handle(self, event):
        if event["type"] == "toggle_play":  # pause game
            self.toggle_pause()

        elif event["type"] == "temp":
            self.toggle_show_temp()

        else:
            raise errors.EventNotHandled(event)

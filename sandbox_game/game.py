from errors import EventNotHandled


class Game():

    def __init__(self, slot=0, pause=False, show_temp=False):
        self.save_slot = slot
        self.pause = pause
        self.show_temp = show_temp

    def toggle_pause(self):
        self.pause = not self.pause

    def toggle_show_temp(self):
        self.show_temp = not self.show_temp

    def handle(self, event):
        if event["type"] == "toggle_play":  # pause game
            self.toggle_pause()

        elif event["type"] == "temp":
            self.toggle_show_temp()

        else:
            raise EventNotHandled(event)

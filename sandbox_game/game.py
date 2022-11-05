class Game():

    def __init__(self, slot=0, pause=False, show_temp=False):
        self.save_slot = slot
        self.pause = pause
        self.show_temp = show_temp

    def toggle_pause(self):
        self.pause = not self.pause

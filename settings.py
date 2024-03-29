import logging
import errors


class Setting:
    def __init__(self, name: str, value: bool, editable: bool = True):
        self.name = name
        self.value = value
        self.default = value
        self.editable = editable

    def toggle(self):
        if self.editable:
            self.value = not self.value
        else:
            logging.warning(f"{self} is not editable")

    def reset(self):
        self.value = self.default

    def __repr__(self) -> str:
        return f"{self.name} setting set to {self.value}"

    def set(self, value: bool):
        self.value = value


def handle_event(event):
    """handle events that change settings"""
    if event["type"] == "toggle_play":  # pause game
        pause.toggle()

    elif event["type"] == "temp":
        showtemp.toggle()
    else:
        raise errors.EventNotHandled(event)


sim_running = Setting("sim_running", False)
showtemp = Setting("temp", False)
pause = Setting("pause", False)
debug = Setting("debug", False)
reset_board = Setting("reset", False)

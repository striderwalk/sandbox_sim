import logging
import errors


class Setting:
    def __init__(self, name: str, value: bool, editable: bool = True):
        self.name = name
        self.value = value
        self.editable = editable

    def toggle(self):
        if self.editable:
            self.value = not self.value
        else:
            logging.warning(f"{self} is not editable")

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


showtemp = Setting("temp", False)
pause = Setting("pause", True)
debug = Setting("debug", False)

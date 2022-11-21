import errors


class Setting:
    """store one setting (thats probaly the word)"""

    def __init__(self, name: str, value: bool) -> None:
        self.name = name
        self.value = value

    def toggle(self) -> None:
        self.value = not self.value


def handle_event(event):
    """handle events that change settings"""
    if event["type"] == "toggle_play":  # pause game
        pause.toggle()

    elif event["type"] == "temp":
        showtemp.toggle()
    else:
        raise errors.EventNotHandled(event)


showtemp = Setting("temp", False)
pause = Setting("pause", False)
showmenu = Setting("menu", False)

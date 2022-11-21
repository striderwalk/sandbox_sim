class Setting:
    def __init__(self, name: str, value: bool) -> None:
        self.name = name
        self.value = value

    def toggle(self) -> None:
        self.value = not self.value


showtemp = Setting("temp", False)
pause = Setting("pause", False)
showmenu = Setting("menu", False)

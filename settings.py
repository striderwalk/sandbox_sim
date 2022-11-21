from enum import Enum, auto


class _settings(Enum):
    # game settings
    SHOWTEMP = auto()
    # SELECETION = auto()/?
    # menu settings
    MENUSHOWN = auto()


class GameSettings:
    # sim settings
    show_temp = False

    # other settings
    show_menu = False

from typing import Callable

from conts import HEIGHT, WIDTH

from .menu_button import Button


def find_size(data):
    "find size that all buttons will occupy"
    maxx, maxy = 0, 0
    for text, _ in data:
        x, y = Button.font.render(text, False, (0, 0, 0)).get_size()

        maxx = max(x, maxx)
        maxy = max(y, maxy)

    button_width = maxx + 50
    button_height = maxy + 50

    return button_width, button_height, maxy


def _make_button(data, xoff, yoff):

    num_buttons = len(data)
    gap = 5

    button_width, button_height, maxy = find_size(data)

    x = WIDTH / 2 - button_width / 2 + xoff
    top_y = HEIGHT / 2 - (maxy + gap * num_buttons) / 2 + yoff
    y_size = button_height + gap

    for index, i in enumerate(data):
        y = top_y + y_size * index
        yield Button(x, y, button_width, button_height, *i)


def make_menu_buttons(data: list, xoff=0, yoff=-100):
    """
    buttons used for action eg start button
    for selection slot_selction.py is used
    """

    return list(_make_button(data, xoff, yoff))

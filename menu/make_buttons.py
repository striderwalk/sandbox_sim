from .menu_button import Button
from .conts import WIDTH, HEIGHT


def make_menu_buttons(data, xoff=0, yoff=-100):
    """
    data = [text: str, func: functions]
    """
    button_num = len(data)
    gap = 5

    # find button size (max_x+50, max_y+50)
    maxx, maxy = 0, 0
    for text, _ in data:
        x, y = Button.font.render(text, True, (0, 0, 0)).get_size()

        maxx = max(x, maxx)
        maxy = max(y, maxy)

    button_width = maxx + 50
    button_height = maxy + 50

    x = WIDTH / 2 - button_width / 2 + xoff
    top_y = HEIGHT / 2 - (maxy + gap * button_num) / 2 + yoff

    return [
        Button(
            x, top_y + (button_height + gap) * index, button_width, button_height, *i
        )
        for index, i in enumerate(data)
    ]

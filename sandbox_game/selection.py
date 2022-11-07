import math
from conts import LOWER_BOARDER, HEIGHT, WIDTH
from sandbox import particles
from errors import EventNotHandled

from .button import Button

CENTER_X = WIDTH / 2


class Selection:
    """
    handle selection buttons
    - check for clicks
    - move buttons
    """

    def __init__(self, index=0):
        self.buttons = []
        # current selection
        self.index = index
        size = LOWER_BOARDER - 5
        for i, obj in enumerate(particles):

            x = size * i
            y = HEIGHT - LOWER_BOARDER + 3
            # button = Button(x, y, size, obj.__name__, obj.colour))
            button = Button(x, y, size, obj.__name__, obj.colour)
            self.buttons.append(button)
        self.buttons[self.index].down()
        # to prevent selection changing when warping
        self.shift((WIDTH - size) / 2)

    def shift(self, num):
        cur_selected = self.buttons[self.index]
        # return
        # move all buttons
        moved_buttons = []
        for button in self.buttons:
            button.move(num, 0)
            moved_buttons.append(button)

        # handle wrapping
        buttons = moved_buttons.copy()
        for button in moved_buttons:
            # check to far to the left
            if button.x + button.size < 0:
                x = buttons[-1].x + button.size
                y = buttons[-1].y
                buttons.remove(button)
                button.move_to(x, y)
                buttons.append(button)

            elif button.x > WIDTH:
                x = buttons[0].x - button.size
                y = buttons[0].y
                buttons.remove(button)
                button.move_to(x, y)
                buttons.insert(0, button)

        last_x = buttons[0].x
        for i in buttons[1:]:
            last_x += i.size
            i.move_to(last_x, i.y)

        self.buttons = buttons
        self.index = self.buttons.index(cur_selected)

    def update(self, win):
        # check for clicks
        clicks = []
        for i, button in enumerate(self.buttons):
            if button.check_click():
                clicks.append(i)

        if clicks:
            self.index = clicks[0]

        for i in self.buttons:
            i.up()

        self.buttons[self.index].down()

        index_x = self.buttons[self.index].rect.center[0]
        diff = CENTER_X - index_x
        if abs(diff) > 5:
            shift = 2 * math.log(abs(diff) + 1)
            self.shift(shift if CENTER_X > index_x else -shift)

        # draw buttons
        for i, button in enumerate(self.buttons):
            button.draw(win)

        return self.index

    def handle(self, event):
        if event["type"] == "left":
            self.index -= 1

        elif event["type"] == "right":
            self.index += 1

        else:
            raise EventNotHandled(event)

        self.index %= len(self.buttons)

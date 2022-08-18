import pygame
from .menu_button import Slot_Button
from .end import end
from .get_slot import get_saved
from .conts import WIDTH, HEIGHT


class Slots:
    """
    a class to handling a set buttons used for selection
     - handle drawing all buttons
     - checking for clicks -> handling click:
         - only allowing one button to be pressed at a times
    """

    def __init__(self):
        gap = WIDTH / 10
        slot_width = 50
        add = (gap - slot_width) / 2
        self.slots = [
            Slot_Button(gap * i + add, HEIGHT - 50, slot_width, 40, f"slot {i}", val, i)
            for i, val in zip(range(10), get_saved())
        ]

    def update(self, win, index):

        # handle draw
        for i, button in enumerate(self.slots):
            button.draw(win)
            if button.clicked:
                index = i
        # check for clicks
        res = []
        for i, button in enumerate(self.slots):
            if button.check_click():
                res.append(i)

        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            if event.type == pygame.KEYDOWN:
                # change selection
                if event.key == pygame.K_LEFT:
                    index -= 1
                if event.key == pygame.K_RIGHT:
                    index += 1
        index %= 10

        # slot selection
        if len(res) == 0:
            res.append(index)
        # set click button
        for i, button in enumerate(self.slots):
            if i != res[0]:
                button.down()
            else:
                index = i
                button.up()

        return index

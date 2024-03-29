import pygame

from conts import HEIGHT, LOWER_BOARDER, WIDTH
from end import end

from .slot_button import Slot_Button


class Slots:
    """
    a class to handling a set buttons used for selection
     - handle drawing all buttons
     - checking for clicks -> handling click:
         - only allowing one button to be pressed at a times
    """

    def __init__(self, saved):
        gap = WIDTH / 10
        slot_width = 50
        add = (gap - slot_width) / 2

        y = HEIGHT - 50
        self.slots = [
            Slot_Button(gap * i + add, y, slot_width, 40, f"slot {i}", val, i)
            for i, val in enumerate(saved)
        ]

    def update(self, win, index):
        pygame.draw.rect(win, (0, 0, 0), (0, LOWER_BOARDER, WIDTH, 3))
        # handle draw
        for i, button in enumerate(self.slots):
            button.draw(win)
            if button.clicked:
                index = i
        # check for clicks
        click = None
        for i, button in enumerate(self.slots):
            if button.check_click() is not None:
                click = i
                break
        if click is None:  # no click
            click = index
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end()
            if event.type == pygame.KEYDOWN:
                # change selection
                if event.key == pygame.K_LEFT:
                    click = (index - 1) % 10
                if event.key == pygame.K_RIGHT:
                    click = (index + 1) % 10

        # set click button
        for i, button in enumerate(self.slots):
            if i != click:
                button.down()
            else:
                index = i
                button.up()

        index %= 10
        return index

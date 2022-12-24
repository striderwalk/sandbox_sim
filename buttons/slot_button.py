import pygame

import fonts


class Slot_Button:
    """
    a class to handle buttons used for selection
     - handle drawing
     - checking for clicks
    """

    font = fonts.get_font(10)

    def __init__(self, x, y, xsize, ysize, name, img, mode):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.name = name
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (xsize, ysize))
        self.mode = mode
        self.xsize, self.ysize = xsize, ysize
        self.clicked = False

    def draw(self, win):
        # draw button on screen

        if self.clicked:
            colour = (255, 0, 0)
        else:
            colour = (0, 0, 0)

        name = Slot_Button.font.render(self.name, False, colour)
        # draw text
        x = self.x + (self.rect.width - name.get_width()) / 2
        y = self.y - 2 - name.get_height()
        win.blit(name, (x, y))
        # draw image (either picture of save of cross)
        pos = (self.rect.topleft[0], self.rect.topleft[1])
        win.blit(self.img, pos)

        # draw box around image
        rect = (self.x - 1, self.y - 1, self.xsize + 2, self.ysize + 2)
        pygame.draw.rect(win, colour, rect, width=2, border_radius=3)

    def check_click(self):
        # check for click
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                return self.mode

    def up(self):
        self.clicked = True

    def down(self):
        self.clicked = False

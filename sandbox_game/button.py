from pathlib import Path
import os
import glob
import pygame
pygame.font.init()
# font = pygame.font.SysFont(None, 24)

font = pygame.font.Font("assets/fonts/joystix monospace.ttf", 10)


# class Button:
#     """
#     a class to represent buttons
#      - handle drawing
#      - handle
#     """

#     def __init__(self, x, y, size, text, colour):
#         self.rect = pygame.Rect((x, y), (size, size))
#         self.rect.topleft = (x, y)
#         self.size = size
#         self.x = x
#         self.y = y
#         self.colour = colour
#         self.text = text
#         self.clicked = False

#     def draw(self, win):
#         # draw button on screen
#         pygame.draw.rect(win, self.colour, self.rect, border_radius=3)
#         if self.clicked:
#             text_colour = (245, 10, 10)
#         else:
#             text_colour = (0, 0, 0)
#         img = font.render(self.text, False, text_colour)
#         win.blit(
#             img,
#             (
#                 self.rect.centerx - img.get_size()[0] / 2,
#                 self.rect.centery - img.get_size()[1] / 2,
#             ),
#         )

#     def check_click(self):
#         action = False
#         pos = pygame.mouse.get_pos()
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] and not self.clicked:
#                 action = True

#         return action

#     def move(self, new_x, new_y):
#         # move by a given amount
#         self.x += new_x
#         self.y += new_y
#         self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
#         self.rect.topleft = (self.x, self.y)

#     def move_to(self, new_x, new_y):
#         # move to somewhere
#         self.x = new_x
#         self.y = new_y
#         self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
#         self.rect.topleft = (self.x, self.y)

#     def up(self):
#         # unclick
#         self.clicked = False

#     def down(self):
#         # click
#         self.clicked = True

# def find_image(name):
#     path = "./assets/buttons/*.png"
#     # "C:\Users\craig\Documents\GitHub\sandbox_sim\assets\buttons>
#     path = "C:/Users/craig/Documents/GitHub/sandbox_sim/assets/buttons/*.png"

#     for i in glob.glob(path):
#         file_name = Path(i).stem
#         if file_name.lower() == name.lower():
#             return i

#     raise ValueError(f"could find image of name {name}")


class Button:
    def __init__(self, x, y, size, name, colour):
        image = pygame.Surface((size, size))
        image.fill((0, 0, 0))
        pygame.draw.rect(image, colour, (1, 1, size - 2, size - 2))
        self.image = image
        self.text = name
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y, size, size))
        self.size = size
        self.clicked = False

    @ property
    def pos(self):
        return self.x, self.y

    def draw(self, win):
        if self.clicked:
            text_color = (255, 0, 0)
        else:
            text_color = (21, 54, 66)

        text = font.render(self.text, False, text_color)
        image = self.image.copy()
        x = (image.get_width() - text.get_width()) / 2
        y = (image.get_height() - text.get_height()) / 2
        image.blit(text, (x, y))
        win.blit(image, self.pos)

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True

        return action

    def move(self, new_x, new_y):
        # move by a given amount
        self.x += new_x
        self.y += new_y
        self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def move_to(self, new_x, new_y):
        # move to somewhere
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def up(self):
        # unclick
        self.clicked = False

    def down(self):
        # click
        self.clicked = True

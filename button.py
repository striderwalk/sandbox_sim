import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 24)
class Button:
    """
    a class to represnt butttons
     - handle drawing
     - handle
    """

    def __init__(self, x, y, size, text, colour):
        self.rect = pygame.Rect((x,y), (size, size))
        self.rect.topleft = (x, y)
        self.colour = colour
        self.text = text
        self.clicked = False

    def draw(self, win):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True

        #draw button on screen
        pygame.draw.rect(win, self.colour, self.rect, border_radius =3)
        if self.clicked:
            img = font.render(self.text, True, (245,10,10))
        else:
            img = font.render(self.text, True, (0,0,0))

        win.blit(img, (self.rect.centerx-img.get_size()[0]/2, self.rect.centery-img.get_size()[1]/2))


        return action


    def up(self):
        self.clicked = False

    def down(self):
        self.clicked = True

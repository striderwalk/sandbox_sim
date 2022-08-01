import pygame
from menu_button import Button
from conts import *

def run(win):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)


    gap = WIDTH/10
    slots = [Button(gap*i+45/2,HEIGHT-30, 45,20, f"slot {i}",i) for i in range(10)]
    while True:
        win.fill((255,255,255))
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255,0,255), pos, 5)
        for i, button in enumerate(slots):
            button.draw(win)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

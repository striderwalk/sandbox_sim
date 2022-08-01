import pygame
from menu_button import Slot_Button
from conts import *
from get_slot import get_saved

def run(win):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)


    gap = WIDTH/10
    button_width = 50
    add = (gap - button_width)/2
    slots = [Slot_Button(gap*i+add,HEIGHT-50, button_width,40, f"slot {i}", val ,i) for i, val in zip(range(10), get_saved())]
    index = 0
    while True:
        win.fill((255,255,255))
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255,0,255), pos, 5)

        # handle slots
        for i, button in enumerate(slots):
            button.draw(win)
            if button.clicked:
                index = i
        # check for clicks
        res = []
        for i, button in enumerate(slots):
            if button.check_click():
                res.append(i)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index -= 1
                if event.key == pygame.K_RIGHT:
                    index += 1
        index %= 10

        if len(res) == 0:
            res.append(index)
        # set click button
        for i, button in enumerate(slots):
            if i != res[0]:
                button.down()
            else:
                index = i
                button.up()

        pygame.display.flip()
        clock.tick()



import pygame
import math
from conts import WIDTH, HEIGHT
from random import randint
def run(win, time=100000):
    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()
 
    img = font.render("LOADING ", True, (160, 0, 0))
    size = img.get_size()
    theata = 0
    dtheata = math.pi/10
    for i in range(min(randint(15, 20), time)):
        win.fill((255,255,255))
        colour = 150
        raidus = 15 
        for i in range(8):
            x = raidus*math.cos(theata-i*dtheata)+((WIDTH+size[0])/2)+20
            y = raidus*math.sin(theata-i*dtheata)+((HEIGHT)/2)
            pygame.draw.circle(win, (colour,colour,colour), (x,y),4)
            colour += 10
            raidus += 0.5
        theata += dtheata

        win.blit(img, ((WIDTH-size[0])/2, (HEIGHT-size[1])/2))
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
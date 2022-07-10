from colour import Color
import pygame
from button import Button

pygame.init()
win =pygame.display.set_mode((800,800))
win.fill((255,255,255))
x = Color("#fc0b03")

b = Button(50,50,50,"penis", (10,255,10))
colours = list(x.range_to(Color("#fc9803"), 100))


for index, j in enumerate(colours):
    pygame.draw.line(win, [i*255 for i in j.rgb], (400,600), (400,100+index),30)


while True:
    b.draw(win)
    pygame.display.flip()

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
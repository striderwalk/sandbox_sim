import pygame
from objects import Air
from conts import * 


class Mouse:
    """
    handle cursor
     - clicks
     - drawing
    """
    def __init__(self, size = 3):
        self.size = size

    def scale(self, num):
        if 0 < self.size <= 50:
            self.size += num

        elif self.size <= 0:
            self.size += 1

        elif self.size >= 50:
            self.size -= 1

    def press(self, board,x,y,obj, keep=False):
        # if keep only replace Air
        # set mouse pos to obj

        board.add_particle(x,y, obj,strict=keep) 

        # set neighbours
        for _, other in board.board[y][x].get_neighbours(board.board, self.size):
            board.add_particle(other.x,other.y, obj,strict=keep)

    def get_pos(self):
        x,y = pygame.mouse.get_pos()
        # return y of COLS*CELL_HEIGHT+10 to avoid boarder bugs
        if y > ROWS*CELL_HEIGHT-3: return ["CORD", x, ROWS*CELL_HEIGHT+10]
        box_x = (x//CELL_WIDTH)
        box_y = (y//CELL_HEIGHT)
        return ["BOX",box_x,box_y]



    def draw_mouse(self, win, obj):
        if obj == Air:
            print("hi")
            colour = (0,0,0)
        else:
            colour = obj.colour
        pygame.mouse.set_visible(False)
        state,x,y = self.get_pos()
        if state == "CORD":
            pygame.mouse.set_visible(True)
            return

        pygame.draw.rect(win, (226, 233, 16), [(x-0.5)*CELL_WIDTH,(y-0.5)*CELL_HEIGHT,CELL_WIDTH*2,CELL_HEIGHT*2])

        pygame.draw.rect(win, colour, [CELL_WIDTH*x-(self.size-1)*CELL_WIDTH,
                                              CELL_HEIGHT*y-(self.size-1)*CELL_HEIGHT,
                                              (self.size*2-1)*CELL_WIDTH, 
                                              (self.size*2-1)*CELL_HEIGHT],
                                              width=1)


    def update(self, win, board, index):
        #print(self.size)
        # check for input
        if pygame.mouse.get_pressed()[0]:
            pos = self.get_pos()
            if pos[0] == "BOX" :
                self.press(board, *pos[1:], particles[index])

        if pygame.mouse.get_pressed()[2]:
            pos = self.get_pos() 
            if pos[0] == "BOX":
                board = self.press(board, *pos[1:], particles[index], keep=True)



        self.draw_mouse(win, particles[index])

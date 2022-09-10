from .sandbox import Box
from .get_particles import particles


def test_placement():
    # check all particle can be added
    board = Box("empty")

    index = 0
    for y, row in enumerate(board.board):
        for x in range(len(row)):
            board.add_particle(x, y, particles[index])
            index = (index + 1) % len(particles)


    return board

def test_update(board):

    # check all particle can be updated

    for row in board.board:
        for i in row:
            i.update(board.board)



def test_board():
    board = test_placement()

    test_update(board)







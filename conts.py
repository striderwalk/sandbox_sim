# all constants
WIDTH, HEIGHT = 840, 707  # board size is 700, 625
LOWER_BOARDER = HEIGHT - 77
UPPER_BOARDER = 35
CELL_WIDTH, CELL_HEIGHT = 7, 7
COLS = int(WIDTH // CELL_WIDTH)
ROWS = int((LOWER_BOARDER) // CELL_HEIGHT)


# def get_factors(num):
#     for i in range(1, num // 2):
#         if num // i == num / i:
#             yield i


# print(WIDTH, LOWER_BOARDER - UPPER_BOARDER)
# x = list(get_factors(WIDTH))
# y = list(get_factors(LOWER_BOARDER - UPPER_BOARDER))
# for i in x:
#     if i in y:
#         print(i)

FPS = 30

# colours

TEXT_COLOUR = (21, 54, 66)
BG_COLOUR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MOUSE_YELLOW = (226, 233, 16)

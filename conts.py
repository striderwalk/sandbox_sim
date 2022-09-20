# all constants
WIDTH, HEIGHT = 840, 705  # board size is 700, 625
LOWER_BOARDER = 75
CELL_WIDTH, CELL_HEIGHT = 7, 7
COLS = int(WIDTH // CELL_WIDTH)
ROWS = int((HEIGHT - LOWER_BOARDER) // CELL_HEIGHT)

FPS = 30
# print(f"{ROWS=}, {COLS=}, {CELL_WIDTH=}, {CELL_HEIGHT=}")

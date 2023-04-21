import logging


def update_sim(board, events=[], mouse_pos=None, pause=False):
    if not pause:
        board.update()

    for event in events:

        if event["type"] == "press":
            board.press(*event["value"])

        elif event["type"] == "rain":
            board.rain_type(event["value"])

        elif event["type"] == "heat":
            board.heat_cells(mouse_pos, *event["value"])

        elif event["type"] == "fix":  # debuging thing
            board.fix()
            if not mouse_pos:
                pass
            x, y = mouse_pos
            logging.info(f"{board.board[y, x]} really at {x=}, {y=}")

    return board

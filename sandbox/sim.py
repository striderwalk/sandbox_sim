import logging


def update_sim(board, fnum, events=[], mouse_pos=None, pause=False):
    if not pause:
        board.update(fnum)

    for event in events:
        if event["type"] == "press":
            board.press(*event["value"])

        elif event["type"] == "rain":
            board.rain_type(event["value"])

        elif event["type"] == "heat":
            board.heat_cells(mouse_pos, *event["value"])

        elif event["type"] == "fix":  # debuging thing
            board.fix()
            if mouse_pos:
                x, y = mouse_pos
                logging.info(f"{board.board[y, x]} really at {x=}, {y=}")

    return board

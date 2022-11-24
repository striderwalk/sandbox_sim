# profiler for project
import cProfile
import pstats
import os
from sandbox import Box, update_sim
from tqdm import tqdm


def time():
    board = Box("profiling")

    for _ in tqdm(range(500)):
        # surf = draw_board(win, board.board, False)
        # win.blit(surf, (0, 0))
        update_sim(board)


print("timeing started please DON'T press anything")
with cProfile.Profile() as pr:
    time()
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="data.prof")
os.system("snakeviz ./data.prof")

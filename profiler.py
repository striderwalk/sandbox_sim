# profiler for project
import cProfile
import os
import pstats

from tqdm import tqdm

from sandbox import Box, update_sim
from sandbox_game.draw import draw_board


def time():
    board = Box("profiling")
    _board = board.board.copy()
    print("running step [1/2]")
    for _ in tqdm(range(500)):

        update_sim(board)
        board.board = _board.copy()
    board = Box("profiling")

    print("running step [2/2]")
    for _ in tqdm(range(500)):
        update_sim(board)


print("timeing started please DON'T press anything")
with cProfile.Profile() as pr:
    time()
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="data.prof")
os.system("snakeviz ./data.prof")

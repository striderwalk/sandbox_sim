# profiler for project
from sandbox_game import time
import cProfile
import pstats
import os

print("timeing started please DON'T press anything")
with cProfile.Profile() as pr:
    time()
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="data.prof")
os.system("snakeviz ./data.prof")

# profiler for project
import cProfile
import pstats
import os
from sandbox_game import time

print("timeing started please DON'T press anything")
with cProfile.Profile() as pr:
    time()
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="data.prof")
os.system("snakeviz ./data.prof")

# profiler for project
from main import main
import cProfile
import pstats
import os
print("timeing started please DON'T press anything")
with cProfile.Profile() as pr:
    main(profiling = True)
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="data.prof")
os.system("snakeviz ./data.prof")
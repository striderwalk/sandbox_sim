from main import main
import cProfile
import pstats
import os
print("timeing started please don't press anything")
with cProfile.Profile() as pr:
    main(timeing = True)
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="hi.prof")
os.system("snakeviz ./hi.prof")
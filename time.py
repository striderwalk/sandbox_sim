from main import main
import cProfile
import pstats
import os

with cProfile.Profile() as pr:
    main(timeing = True)

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.dump_stats(filename="hi.prof")
os.system("snakeviz ./hi.prof")
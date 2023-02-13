import json
from colour import Color

cbase = "#fc9803"


# heatmap -------------------------------->

# below 0 to about 30 degrees
m1 = list(Color("#0000ff").range_to(Color("#00ffd4"), 75))
m2 = list(Color("#00ffd4").range_to(Color("#88ff00"), 140))
m3 = list(Color("#88ff00").range_to(Color("#ff0000"), 500))

HEAT_MAP = m1 + m2 + m3


HEAT_MAP = [[round(i * 255, 2) for i in colour.rgb] for colour in HEAT_MAP]
# fire stuff
base = Color(cbase)
FIRE_COLOURS = base.range_to(Color("#fc0b03"), 5)
FIRE_COLOURS = list(FIRE_COLOURS)
FIRE_COLOURS = [[round(i * 255, 2) for i in colour.rgb] for colour in FIRE_COLOURS]

colour_values = {"FIRE_COLOURS": FIRE_COLOURS, "HEAT_MAP": HEAT_MAP}
with open("D:/sandbox_sim/assets/colour_data.json", "w") as file:
    json.dump(colour_values, file, indent=2)

"this file cotains lots of data"


ROOM_TEMP = 22
MAX_TEMP = 10_000
MIN_TEMP = -2_000


#
# temp in celsius
# mass for 1cm³ in grams
# conduct is SHC in J/kg


acid_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": 110,
    "mass": 1,
    "conduct": 0.6,
}


air_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": MAX_TEMP,
    "mass": 0.01,
    "conduct": 1.2,
}


ash_vals = {
    "start_temp": 400,
    "min_temp": MIN_TEMP,
    "max_temp": 600,
    "mass": 0.61,
    "conduct": 0.46,
}

fire_vals = {
    "start_temp": 650,
    "min_temp": 20,
    "max_temp": MAX_TEMP,
    "mass": 0.9,
    "conduct": 10,
}

fume_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": MAX_TEMP,
    "mass": 0.01,
    "conduct": 0.025,
}

gren_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": MAX_TEMP,
    "mass": 3,
    "conduct": 1.8,
}

ice_vals = {
    "start_temp": -10,
    "min_temp": MIN_TEMP,
    "max_temp": 0,
    "mass": 0.92,
    "conduct": 2.5,
}

lava_vals = {
    "start_temp": 2000,
    "min_temp": 1000,
    "max_temp": MAX_TEMP,
    "mass": 6,
    "conduct": 12,
}

sand_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": 2000,
    "mass": 12,
    "conduct": 0.0025,
}

smoke_vals = {
    "start_temp": 600,
    "min_temp": MIN_TEMP,
    "max_temp": MAX_TEMP,
    "mass": 2.4,
    "conduct": 1,
}

steam_vals = {
    "start_temp": 150,
    "min_temp": 100,
    "max_temp": MIN_TEMP,
    "mass": 0.75,
    "conduct": 0.0211,
}

stone_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": 2000,
    "mass": 3,
    "conduct": 1.8,
}

water_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": 0,
    "max_temp": 100,
    "mass": 1,
    "conduct": 0.6,
}

wood_vals = {
    "start_temp": ROOM_TEMP,
    "min_temp": MIN_TEMP,
    "max_temp": 200,
    "mass": 1.5,
    "conduct": 0.1,
}

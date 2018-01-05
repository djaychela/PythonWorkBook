from math import pi

def sphere_volume(h, r=10):
    vol = (4 * pi * (r**3)) / 3
    air_vol = (pi * (h**2) * (3 * r - h)) / 3
    return vol - air_vol

print(sphere_volume(2))
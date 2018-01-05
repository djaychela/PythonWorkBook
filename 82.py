import ephem

j = ephem.Jupiter()
print(j.name)
j.compute('1230/1/1')
print(j.sun_distance*ephem.meters_per_au/1000)


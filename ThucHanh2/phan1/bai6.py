temps = [25.2,  16.8,  31.4,  23.9,  28,  22.5,  19.6]
print(temps)
temps.sort()
print(temps)
cool_temps = temps[0:2]
print(cool_temps)
warm_temps = temps[2:None]
print(warm_temps)
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)
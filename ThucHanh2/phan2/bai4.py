alkaline_earth_metals = [
    [4, 9.012], 
    [12, 24.305],
    [20, 40.078],
    [38, 87.62],
    [56, 137.327],
    [88,226]
]
print(alkaline_earth_metals)

for u  in alkaline_earth_metals:
    for v in u:
        print(v,end = " ")
    print("\n")

number_and_weight = []
for u  in alkaline_earth_metals:
    for v in u:
        number_and_weight.append(v)

print(number_and_weight)
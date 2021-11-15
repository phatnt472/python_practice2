def km_to_miles(km):
    return km/1.6

km = float(input("Nhập vào số km muốn đổi: "))
print("{} km = {} miles".format(km, km_to_miles(km)))
import random
rat_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
rat_2 = [2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.1, 10.2, 11.8]


if rat_1[0]<rat_2[0]:
    print("Chuột 1 nhẹ hơn chuột 2 ngày 1.")
else:
    print("Chuột 1  nặng hơn chuột 2  ngày 1.")

if rat_1[9] > rat_2[9] and rat_1[0] > rat_2[0]:
   print("Chuột 1 vẫn nặng hơn chuột 2-")
else:
   print("Chuột 2 trở nên nặng hơn chuột 1.")

if rat_1[0] > rat_2[0]:
    print("Chuột 1 nặng hơn chuột 2 ngày 1.")
    if rat_1[-1] > rat_2[-1]:
        print("Chuột 1 vẫn nặng hơn chuột 2.")
    else:
        print("Chuột 2 trở nên nặng hơn chuột 1")
else:
    print("Chuột 1  nặng hơn chuột 2  ngày 1.")


def avg_top_3(grade1, grade2, grade3,grade4):
    arr = [grade1, grade2, grade3, grade4]
    arr.sort()
    return (arr[3]+arr[2]+arr[1])/3

grade1 = float(input("Nhập điểm môn 1: "))
grade2 = float(input("Nhập điểm môn 2: "))
grade3 = float(input("Nhập điểm môn 3: "))
grade4 = float(input("Nhập điểm môn 4: "))

print(avg_top_3(grade1, grade2, grade3, grade4))
def avg_grade(grade1,grade2,grade3):
    return (grade1+ grade2 + grade3)/3

grade1 = float(input("Nhập điểm môn 1: "))
grade2 = float(input("Nhập điểm môn 2: "))
grade3 = float(input("Nhập điểm môn 3: "))
print(f'Điểm trung bình 3 môn: {avg_grade(grade1,grade2,grade3)}')
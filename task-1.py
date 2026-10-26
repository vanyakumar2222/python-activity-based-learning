
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    subject = float(input("Enter subject marks: "))
    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    if marks >= 75 and subject >= 50 and attendance >= 75 and income <= 200000:
        students.append([name, marks, attendance, income])
        print("Eligible")
    else:
        print("Not Eligible")

students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\nScholarship Ranking:")

for rank, s in enumerate(students, 1):
    print(rank, s[0], s[1], s[2], s[3])


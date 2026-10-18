students = []

for i in range(int(input())):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set(student[1] for student in students))
second_lowest = grades[1]

names = sorted(student[0] for student in students if student[1] == second_lowest)

for name in names:
    print(name)


students = {}

n = int(input("Ввдедите количество студентов: "))

for i in range(n):
    name_students = input("Введите имя студента: ")
    grade_students = input("Введите оценки студента через пробел: ")
    grade = [float(grade) for grade in grade_students.split()]
    students[name_students] = grade

print('\nРезультаты: ')
for student, grade in students.items():
    average = sum(grade) / len(grade)
    print(f"{student}: средний балл - {average:.2f}")

best_student = None
best_grade = 0

for student, grade in students.items():
    average = sum(grade) / len(grade)
    if average > best_grade:
        best_student = student
        best_grade = average

print(f"\nЛучший студент: {best_student}, средний балл - {best_grade:.2f} ")

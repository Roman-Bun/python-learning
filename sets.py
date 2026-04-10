# 1. Створи список з повторюваними числами:
#    [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]
my_list = [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]
# 2. Перетвори на set і виведи унікальні числа
my_set = set(my_list)
print(my_set)
# 3. Створи два set:
students_python = {"Roman", "Ivan", "Olena", "Dmytro"}
students_js = {"Ivan", "Anna", "Olena", "Taras"}
# 4. Виведи студентів які вчать ОБИДВА курси
common = students_python & students_js
print(common)
# 5. Виведи студентів які вчать ТІЛЬКИ Python
only_python = students_python - common
print(only_python)
# 6. Виведи ВСІХ студентів (без повторень)
students = students_python.union(students_js)
print(students)
# 7. Перевір чи є "Roman" в students_js
student = "Roman"
if student in students_js:
    print("Присутній")
else:
    print("Відсутній")
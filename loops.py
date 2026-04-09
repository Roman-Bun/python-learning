# 1. Виведи числа від 1 до 10
for i in range(1, 11):
    print(i)
# 2. Виведи тільки парні числа від 1 до 20
for i in range(2, 21, 2):
    print(i)
# 3. Порахуй суму чисел від 1 до 100
total = 0
for i in range(1, 101):
    total += i
print(total)
# 4. Виведи таблицю множення для числа 5
number = 5
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
# 5. Попроси користувача вгадати число 7,
#    повторюй поки не вгадає (while loop)
guess = 0
while guess != 7:
    guess = int(input("Вгадай число! "))
print("Молодець, правильне число 7!")
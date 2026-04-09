# 1. Створи список з 5 імен друзів
names = ["Roman", "Artem", "Viktoriya", "Yuriy", "Angela"]
# 2. Додай нового друга в кінець
names.append("Olena")
# 3. Додай друга на початок (індекс 0)
names.insert(0, "Florian")
# 4. Видали другого друга зі списку
names.pop(1)
# 5. Виведи список відсортований за алфавітом
names.sort()
print(names)
# 6. Виведи тільки перших 3 друзів (slice)
print(names[:3])
# 7. За допомогою list comprehension створи
#    новий список де всі імена великими літерами
new_names = [name.upper() for name in names]
print(new_names)
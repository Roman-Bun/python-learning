# 1. Створи словник студента:
#    імʼя, вік, місто, список курсів
student = {
    "name": "Roman",
    "age": 33,
    "city": "Kyiv",
    "courses": ["Python", "Git"]
}

# 2. Виведи імʼя і місто студента
print(student["name"])
print(student["city"])

# 3. Додай email студента
student["email"] = "roman@gmail.com"

# 4. Зміни вік студента
student["age"] = 34

# 5. Виведи всі ключі словника
for key in student.keys():
    print(key)

# 6. Виведи всі пари ключ: значення
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Створи dict comprehension:
dict_1 = {"Roman": 95, "Ivan": 87, "Olena": 92}

#    → новий словник де оцінки збільшені на 5
dict_2 = {name: score + 5 for name, score in dict_1.items()}
print(dict_2)

# 8. Перевір чи є ключ "phone" в словнику
print("phone" in student)

user = {
    "name": "Roman",
    "scores": [95, 87, 92],
    "address": {
        "city": "Kyiv",
        "street": "Khreshchatyk"
    }
}
# Як отримати:

# Середню оцінку зі списку scores?
# Назву міста з вкладеного словника?

print(sum(user["scores"]) / len(user["scores"]))
print(user["address"].get("city"))


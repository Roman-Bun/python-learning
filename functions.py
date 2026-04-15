# 1. Напиши функцію make_order(dish, quantity, city="Kyiv")
#    яка виводить:
#    "Замовлення: 2x Піца, доставка в Kyiv"
def make_order(dish, quantity, city="Kyiv"):
    print(f"Замовлення: {quantity}x {dish}, доставка в {city}")

make_order("Піца", 2)

# 2. Напиши функцію total_price(*prices)
#    яка приймає довільну кількість цін
#    і повертає їх суму
def total_price(*prices):
    total = sum(prices)
    return total

print(total_price(2, 4, 5, 7))

# 3. Напиши функцію create_user(**kwargs)
#    яка приймає довільні дані користувача
#    і виводить кожне поле
def create_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_user(name="Roman", age=25, city="Kyiv")
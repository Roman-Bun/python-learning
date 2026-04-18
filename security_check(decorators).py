user_role = "admin"
balance = 1000

def check_access(func):
    def wrapper(*args, **kwargs):
        if user_role == "admin":
            print("Доступ дозволено")
            return func(*args, **kwargs)
        else:
            print("ПОМИЛКА: Немає прав доступу")
    return wrapper

@check_access
def withdraw_money(money):
    global balance
    balance = balance - money
    print(f"Гроші {money} успішно знято! 💸")
    print(f"Ваш баланс: {balance}")

withdraw_money(100)
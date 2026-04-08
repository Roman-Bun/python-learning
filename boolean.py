age = int(input("Введіть вік: "))
has_ticket = input("Є квиток? (yes/no): ") == "yes"
is_vip = input("VIP статус? (yes/no): ") == "yes"

if (age >= 18 and has_ticket) or is_vip:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")

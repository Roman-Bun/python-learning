def make_saver():
    balance = 0
    def add_money(amount):
        nonlocal balance
        balance = amount + balance
        return balance
    return add_money

my_savings = make_saver() 

print(my_savings(100))  # Має вивести: 100
print(my_savings(50))   # Має вивести: 150 (бо 100 + 50)
print(my_savings(200))  # Має вивести: 350
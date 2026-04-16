def print_user(name, age):
    print(f"User: {name}, {age}")

def calculate_discount(price):
    return price * 0.8

def save_price(price):
    with open("out.txt", "w") as f:
        f.write(str(price))

print_user("Roman", 33)
discounted = calculate_discount(100)
print(discounted)
save_price(discounted)
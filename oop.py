class Smartphone():
    def __init__(self, brand, model, price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.brand = brand
        self.model = model
        self.__price = price

    @classmethod
    def from_string(cls, data):
        brand, model, price = data.split("-")
        return cls(brand, model, int(price))
    
    @property
    def price(self):
        return f"{self.__price} грн."
    
    def __str__(self):
        return f"Смартфон бренду {self.brand}, модель {self.model}"
    
    def __eq__(self, other):
        return self.brand.lower() == other.brand.lower()
    
phone1 = Smartphone("Samsung", "Galaxy S24", 45000)
phone2 = Smartphone("Apple", "iPhone 15", 52000)
phone3 = Smartphone("Samsung", "Galaxy S23", 38000)

print(phone1)
print(phone2)
print(phone2.price)
print(phone1 == phone2)
print(phone1 == phone3)

new_phone = Smartphone.from_string("Apple-iPhone15-52000")
print(new_phone)
print(new_phone.price)

try:
    bad_phone = Smartphone("Nokia", "3310", -100)
except ValueError as e:
    print(e)
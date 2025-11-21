from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79990000001"),
    Smartphone("Samsung", "Galaxy S21", "+79990000002"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79990000003"),
    Smartphone("Huawei", "P40", "+79990000004"),
    Smartphone("Nokia", "3310", "+79990000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

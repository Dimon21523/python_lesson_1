from smartphone import smartphone

catalog = []

catalog.append(smartphone("Apple", "iPhone 13", "+7999000001"))
catalog.append(smartphone("Samsung", "Galaxy S21", "+7999000002"))
catalog.append(smartphone("Google", "Pixel 6", "+7999000003"))
catalog.append(smartphone("Xiaomi", "Redmi Note 10", "+7999000004"))
catalog.append(smartphone("Huawei", "P50 Pro", "+7999000005"))

for phone in catalog:
    print(f{phone.brand} {phone.model} - {phone.phone_number})
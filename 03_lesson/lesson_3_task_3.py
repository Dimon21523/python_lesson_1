from address import Address
from mailing import Mailing

from_addr = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="1",
    apartment="10",
)

to_addr = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="20",
    apartment="5",
)

mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350.75,
    track="TRACK123456789",
)

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)

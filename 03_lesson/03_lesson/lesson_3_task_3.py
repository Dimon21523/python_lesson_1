from address import Address
from mailing import Mailing

to_addr = Address(
    "123455",
    "New York",
    "5th Avenue",
    "10B",
    "25"
)
from_addr = Address(
    "543210",
    "Los Angeles",
    "Sunset Boulevard",
    "20A",
    "10"
)
mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350.75,
    track="TRACK123456789"
)

ptint(
      f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)

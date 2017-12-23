# from mlab import mlab_connect
# from Models.service import Service
# from random import randint, choice
# mlab_connect()
#
# Service.drop_collection()
#
# for _ in range(7):
#     service = Service(account = choice([new_lol_accounts]),
#                       password = randint(100, 999),
#                       game = "lol",
#                       price = choice(["1000/h", "1500/h", "2000/h"]),
#                       contact = 0 + randint(100000000, 999999999),
#                       occupied = choice([True, False]))
#     service.save()

from mlab import mlab_connect
from Models.service import Service
from faker import Faker
from random import randint, choice

service_faker = Faker()
mlab_connect()
Service.drop_collection()

for _ in range(30):
    service = Service(account = service_faker.name(),
                      game = choice(["lol", "csgo", "pubg"]),
                      price = choice(["1000/h", "1500/h", "2000/h"]),
                      contact = 0 + randint(100000000, 999999999),
                      password = randint(100, 999),
                      occupied = choice([True, False]))
    service.save()

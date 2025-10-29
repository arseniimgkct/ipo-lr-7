# Арсений Жук
import json

print("start code ...")

qualif = print("Введите номер квалификации: ")

with open("dump.json") as file:
    data = dict(json.load(file))
    

print("end code ...")
# Арсений Жук
import json

print("start code ...")

qualification = input("Введите номер квалификации: ")

with open("dump.json", encoding="utf-16") as file:
    data = json.load(file)

for item in data:
    model = item.get("model")
    if model in ("data.skill", "data.specialty"):
        fields = item.get("fields", {})
        code = fields.get("code")

        if code == qualification:
            print(' Найдено '.center(40,"="))
            print(f'{code} >> Специальность {fields.get("title")}, {fields.get("c_type")} ')
            found = True

if not found:
    print("Не найдено")

print("end code ...")
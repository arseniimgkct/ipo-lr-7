# Арсений Жук
import json

print("start code ...")

qualif_number = input("Введите номер квалификации: ")

with open("dump.json", encoding="utf-16") as file:
    data = json.load(file)

found = False
for item in data:
    model = item.get("model")
    if model in ("data.skill", "data.specialty"):
        fields = item.get("fields", {})
        code =  fields.get("code")

        if code == qualif_number:
            print(' Найдено '.center(40,"="))
            ctype = fields.get("c_type")
            ctype = ', ' + ctype if ctype != None else ""
            qualif = "Специальность" if model == "data.specialty" else "Квалификация"
            print(f'{code} >> {qualif} "{fields.get("title")}"{ctype} ')
            found = True

if not found:
    print("Не найдено".center(40, "="))

print("end code ...")
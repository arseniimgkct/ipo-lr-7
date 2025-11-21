# Арсений Жук
import json
import os

print("start code ...")

class City:
    def __init__(self, id, name, country, people_count):
        self.id = id
        self.name = name
        self.country = country
        self.is_big = True if people_count > 100_000 else False
        self.people_count = people_count
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "people_count": self.people_count,
            "is_big": self.is_big
        }
        

menu = """
1. Вывести все города
2. Вывести город по id
3. Добавить город
4. Удалить город
5. Выйти из программы
"""

def open_file():
    if not os.path.exists("db.json"):
        with open("db.json", "w", encoding="utf-8") as f:
            f.write("[]")

    with open("db.json", "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except:
            data = []
            
    return data

def output_cities():
    print("Список Городов".center(40, "-"))
    for city in data:
        print(f'{city["id"]}. {city["name"]}, {city["country"]} - {city["people_count"]} | {"Большой" if city["is_big"] else "Небольшой"}')

def output_city_by_id():
    city_id = int(input("Введите id для поиска:"))
    for city in data:
        if city_id == city["id"]:
            print(f'{city["id"]}. {city["name"]}, {city["country"]} - {city["people_count"]} | {"Большой" if city["is_big"] else "Небольшой"}')
            break
    else:
        print("Не найден город с таким id")        

def add_city():
    name = input("Введите название города: ")
    country = input("Введите страну: ")
    people_count = int(input("Введите численность населения: "))
            
    id = data[-1]["id"] + 1 if data else 1                
    city = City(id, name, country, people_count)
    data.append(city.to_dict())
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Город успешно добавлен")

def delete_city():
    city_id = int(input("Введите id города: "))
    for i in range(0, len(data)):
        if data[i]["id"] == city_id:
            del data[i]
            break
    else:
        print("Город с таким id не найден")
        return
            
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        print("Город успешно удален")

actions = 0

data = open_file()

while True:
    print(menu)
    num = int(input("Выберите действие: "))
    actions += 1
    
    match num:
        case 1:
            if not data:
                print("Список пуст")
                continue
            output_cities()
        case 2:
            output_city_by_id()
        case 3:
            add_city()
        case 4:
            delete_city()
        case 5:
            print(f'Выполнено операций: {actions}')
            break
        
        case _: 
            print("Некорректное действие")
            
print("end code ...")
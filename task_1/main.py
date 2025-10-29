# Арсений Жук

print("start code ...")

books = [
    {
    "title": "Lorem",
    "author": "Lorem",
    "year": 2000,
    }, 
        {
    "title": "Lorem",
    "author": "Lorem",
    "year": 2000,
    }, 
        {
    "title": "Lorem",
    "author": "Lorem",
    "year": 2000,
    }, 
        {
    "title": "Lorem",
    "author": "Lorem",
    "year": 2000,
    }, 
        {
    "title": "Lorem",
    "author": "Lorem",
    "year": 2000,
    }, 
]

for i in range(len(books)):
    print(f'Книга: {books[i].get("title")}'.center(40, "-"))
    print(f'Название: {books[i].get("title")}, Автор: {books[i].get("author")}')
    print(f'{books[i].get("year")}'.center(40, "-"))
    print()


print("end code ...")
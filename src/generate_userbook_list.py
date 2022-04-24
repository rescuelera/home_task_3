from csv import DictReader
import json
from src import utils

with open('../data/books.csv', newline='') as f:
    reader = DictReader(f)
    header = next(reader)
    books = []
    for book in reader:
        books.append(book)


def list_generator():
    for elem in books:
        yield elem


book_iter = list_generator()

with open('../data/users.json', "r") as f:
    users = json.load(f)
    len_users = len(users)

people_max_book, people_min_book, max_book_count, min_book_count = utils.get_books_for_people_count(len(books),
                                                                                                    len_users)

result_dict = []
# repeat 29 and 32
user_intervals = [(0, people_max_book, max_book_count),
                  (people_max_book, people_max_book + people_min_book, min_book_count)]

l = [(1, 2), (3, 4)]
for a, b in l:
    pass
for begin_user, end_user, book_count in user_intervals:

    for i in range(begin_user, end_user):
        user = {
            "name": users[i]["name"],
            "gender": users[i]["gender"],
            "address": users[i]["address"],
            "age": users[i]["age"],
            "books": []
        }
        for j in range(book_count):
            book_info = next(book_iter)
            book = {
                "title": book_info["Title"],
                "author": book_info["Author"],
                "pages": book_info["Pages"],
                "genre": book_info["Genre"]
            }
            user["books"].append(book)
        result_dict.append(user)

with open('../data/result.json', "w") as f:
    json.dump(result_dict, f, indent=4)

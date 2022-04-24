def get_books_for_people_count(book_count: int, people_count: int) -> (int, int, int, int):
    min_book_count = book_count // people_count
    people_max_book = book_count % people_count
    people_min_book = people_count - people_max_book
    max_book_count = min_book_count + 1

    return people_max_book, people_min_book, max_book_count, min_book_count

import json
from copy import copy


class Book:
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)

  def __str__(self):
    return self.title

  def __repr__(self):
    return str(self)


def get_books(filename, raw=False):
  try:
    data = json.load(open(filename))
  except FileNotFoundError:
    return []
  else:
    if raw:
      return data['books']
    return [Book(**book) for book in data['books']]


BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)


### SORTED ###
# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
# pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

# important_list = [5, 3, 1, 2, 4]
# important_list.sort()  # Bad idea, sorts list in place
# sorted(important_list)  # Sorts a copy of the list

### MAP ###
def sales_price(book):
  """Apply a 20% discount to the book's price"""
  book = copy(book)
  book.price = round(book.price - book.price * .2, 2)
  return book


# sales_books = list(map(sales_price, BOOKS))
# sales_books2 = [sales_price(book) for book in BOOKS]

### FILTER ###
def is_long_book(book):
  """Does a book have 600+ pages?"""
  return book.number_of_pages >= 600


long_books = list(filter(is_long_book, BOOKS))
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
print(len(BOOKS))
print(len(long_books2))
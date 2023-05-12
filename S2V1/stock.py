import json


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
    return data['books'] if raw else [Book(**book) for book in data['books']]


BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
# print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
# pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
# print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

# important_list = [5, 3, 1, 2, 4]
# important_list.sort()  # Bad idea, sorts list in place
# sorted(important_list)  # Sorts a copy of the list

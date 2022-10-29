import csv

# Read CSV file
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

#----------------------------------------------

import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
print(isbn_list)

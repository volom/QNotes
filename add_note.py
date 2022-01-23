import os
import re
from db_repo.db_handle import *

with open('categories.txt', 'r') as f:
    f = f.read()
    lst_cat = f.split('\t')
    lst_cat = [x for x in lst_cat if x != '']

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def enumerate_cb(db_info):
    enumbers = list(enumerate(db_info))
    
    return enumbers, ' - '.join([str(j) for i in enumbers for j in i])

cats = enumerate_cb(get_cat())[0]
print(enumerate_cb(lst_cat)[1])


while True:
    books = enumerate_cb(get_books())[0]
    print("(!) To add note use given template - |{number_cat}\\t{note}|\n")
    print("(!) To add book note use given template - |b\\t{number_cat}\\t{number_book|book_name_manual}\\t{note}|\n")

    print("-------------------------")
    print(f'categories - {enumerate_cb(lst_cat)[1]}')
    print("-------------------------")
    print(f'books - {enumerate_cb(get_books())[1]}')

    while True:
        note = input("Add note---> ")
        try:
            try:
                re.match(r'\d{1,100}\t.*', note).group(0)
            except:
                re.match(r'b\t\d{1,100}\t(\d{1,100}|.*)\t.*', note).group(0)
        except:
            print("Please use given format")
            continue
        else:
            break
    comment = input("Add comment if any---> ")
    # add to info to sql db
    try:
        re.match(r'\d{1,100}\t.*', note).group(0)
        note = note.split('\t')
        category = [x[1] for x in cats if x[0] == int(note[0])][0]
        add2db('notes', ('category', 'note', 'comment'), (category, note[1], comment))
    except:
        try:
            re.match(r'b\t\d{1,100}\t\d{1,100}\t.*', note).group(0)
            note = note.split('\t')
            category = [x[1] for x in cats if x[0] == int(note[1])][0]
            book = [x[1] for x in books if x[0] == int(note[2])][0]
            add2db('notes', ('category', 'note', 'comment', 'liter'), (category, note[1], comment, book))
        except:
            note = note.split('\t')
            category = [x[1] for x in cats if x[0] == int(note[1])][0]
            book = note[2]
            add2db('notes', ('category', 'note', 'comment', 'liter'), (category, note[1], comment, book))

    clearConsole()

    print(f"The note - |{note}| - was added successfully")


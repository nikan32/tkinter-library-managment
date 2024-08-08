import json

class Book :
    def __init__(self,name,id, year,author):
        self.name = name
        self.year = year
        self.author = author
        self.id = id
class Library:
    def __init__(self):
        self.database = json.load(open('managmentlibery\database.json'))
    def add_book(self):
        pass
    def remove_book(self):
        pass
    def search_book(self):
        pass
    def get_all_book(self):
        pass
       
#library = Library()
#print(library.database['id001'])
import json

class Book :
    def __init__(self,name,id, year,author):
        self.name = name
        self.year = year
        self.author = author
        self.id = id
        def get_key_val(self):
            key_value={
                "name":self.name,
                "year":self.year,
                "author":self.author
             }
            return key_value




class Library:
    def __init__(self):
        self.database = json.load(open('managmentlibery\database.json'))

    
    def add_book(self, id, name, year, author):
        if id in self.database.keys():
            raise ValueError('id already exists')
        else:
            newBook=(id, name, year, author)
            self.database[id] = newBook.get_key_val()
            json.dump(
                self.databse,
                open("./database.json","w"),
                indent=4
            )
    
    
    def remove_book(self):
        pass
    
    
    
    def search_book(self):
        pass
    
    
    def get_all_book(self):
        pass
       
#library = Library()
#print(library.database['id001'])
Library.add_book(
    "id0004",   
    "harrypotter 4",
    2005,
    "j.k.rolling"
)
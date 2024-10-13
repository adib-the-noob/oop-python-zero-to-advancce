class Book:
    def __init__(self, name, author, num_pages):
        self.name = name
        self.author = author 
        self.num_pages = num_pages
        
    def __eq__(self, value: object) -> bool:
        return self.num_pages == value.num_pages
        
    def __lt__(self, value: object) -> bool:
        return self.num_pages < value.num_pages
    
    def __contains__(self, value: object) -> bool:
        return value in self.name # for searching any value in this class in name
        
    def __getitem__(self, key: object):
        if key == 'name':
            return self.name
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"{key} is not a valid key"
        
book1 = Book("Python for Beginners", "John Doe", 300)
book2 = Book("Python for Intermediate", "Jane Doe", 400)
book3 = Book("Python for Advanced", "Alice Doe", 500)

print(book1 == book2) # False
print(book1 < book2) # True
print("Python" in book1) # True

print()
print(book1['name']) # Python for Beginners
print(book1['author']) # John Doe
print(book1['hacker']) # 300
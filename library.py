class Library:
    def __init__(self,capacity):
        self.capacity = capacity
        self.users = []

    class Book:
        def __init__(self,maxBooks):
            self.maxBooks = maxBooks
            self.books = []

        def free_space(self):
            return self.maxBooks - len(self.books)

        def add_book(self,title):
            if not self.free_space():
                return False
            self.books.append(title)
            return True

    def add_user(self,name):
        if not self.free_spots():
            return False
        self.users.append(name)
        return True

    def free_spots(self):
        return self.capacity - len(self.users)

library = Library(2)

users = ["Anita" , "Anda", "Teo"]
books1 = ["Maitrey" , "Lord of The Flies", "Crime and Punishment"]
books2 = ["Papillon", "Hamlet"]
books3 = ["The Boy in striped pajamas"]

for user in users:
    if library.add_user(user):
        print(f"Added {user} to the Library")
    else:
        print(f"No spots available for {user}")

class Library:
    def __init__(self,capacity):
        self.capacity = capacity
        self.users = []

    def add_user(self,name):
        if not self.free_spots():
            return False
        self.users.append(name)
        return True

    def free_spots(self):
        return self.capacity - len(self.users)

library = Library(2)

users = ["Anita" , "Anda", "Teo"]

for user in users:
    if library.add_user(user):
        print(f"Added {user} to the Library")
    else:
        print(f"No spots available for {user}")

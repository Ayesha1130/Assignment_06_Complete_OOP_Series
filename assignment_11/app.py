# Class Methods
# Create a class Book with a class variable total_books. Add a class method 
# increment_book_count() to increase the count when a new book is added.

class Book():
    # Class variable jo sab books ke liye common hai
    total_book = 0

    def __init__(self,title):
        self.title = title # Har book ka title alag ho
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1 # Class variable ko 1 add hoga

book1 = Book("Python Basic")
book2 = Book("Python Advance")

# Output mein dono book titles aur total count show kiya
print("Book 1 Title:", book1.title)
print("Book 2 Title:", book2.title)
print("Total Books", Book.total_book)







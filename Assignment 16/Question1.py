class Book:
    count = 0
    def __init__(self, bid=None, bname=None, price=0, author=None ):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print(f"Book object created.Remaing count: {Book.count}")

    def __del__(self):
        Book.count -= 1
        print(f"Book object deleted. Remaining count: {Book.count}")

    def showBook(self):
        print(f"Book id = {self.bid}")
        print(f"Bookname = {self.bname}")
        print(f"Bookprice = {self.price}")
        print(f"Bookauthor = {self.author}")

b1 = Book()
b2 = Book(101, "clanguage", 450, "denis riche")

b1.showBook()
b2.showBook()

print(f"\ntotal number of Book objects created: {Book.count}")

    

class Book:
    def __init__(self, bid, bname,prize,author ):
        self.bid = bid
        self.bname = bname
        self.prize = prize
        self.author = author
        print("constructor called:Book object created")

    def __del__(self):
        print("destructor called: Book'{self.bname}' object destroyed.")

    def showBook(self):
        print("bid:",self.bid)
        print("bname:",self.bname)
        print("prize:",self.prize)
        print("author:",self.author)

Book1 = Book("python programing",500,"gudio van rossum")
Book1.showBook()


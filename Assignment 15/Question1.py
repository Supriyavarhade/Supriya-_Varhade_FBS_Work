class Book:
    def __init__(self, id = "none", nm = "none", price = 0, author = "none"):
      self.bid = id
      self.bname = nm
      self.bprice = price
      self.author = author

    def showbook(self):
        print("ID:",self.bid)
        print("Name:",self.bname)
        print("Price:",self.bprice)
        print("Author:",self.author)

    def __del__(self):
        print("Book is Destroyed.")

b1 = Book(101,"ABC",500, "XYZ")
b1.showbook()
del b1
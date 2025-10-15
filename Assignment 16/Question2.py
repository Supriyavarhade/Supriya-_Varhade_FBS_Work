class product:
    def __init__(self, pid=None, pname=None, price=None, Quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.Quantity = Quantity
        print(f"product object created:")

    def __del__(self):
        print(f"product object with id{self.pname} is deleted.")

    def showproduct(self):
        print(f"product id = {self.pid}")
        print(f"product name = {self.pname}")
        print(f"price = {self.price}")
        print(f"Quantity = {self.Quantity}")

    def applydiscount(self):
        if self.price is not None:
            discount_amount = (product.discount / 100) * self.price
            self.price -= discount_amount
            print(f"discount of{product.discount}% applied")
        else:
            print("price not set. cannot apply discount.")

p1 = product()
p2 = product(201, "laptop", 50000, 2)

p1.showproduct()
p2.showproduct()

class Product:
    def __init__(self, pid="0", pname="0", price="0", quantity="0"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("pid:", self.pid)
        print("pname:",self.pname)
        print("price:", self.price)
        print("quantity:", self.quantity)

    def __del__(self):
        print("Product is destroyed")

P1 = Product( "23", "supriya", 2300, 2 )   
P1.showProduct()
del P1

P2 = Product()
P2.showProduct()
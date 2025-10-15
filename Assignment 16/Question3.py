class Shirt:
    
    size_price_increase = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }
    def __init__(self, sid=None, sname=None, type=None, price=None, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print(f"Shirt object created: {self.sname if self.sname else 'Unnamed Shirt'}")

        if self.price is not None:
            self.applySizePrice()

    def __del__(self):
        print(f"Shirt object with ID {self.sid} is deleted.")

    def applySizePrice(self):
        if self.size.lower() in Shirt.size_price_increase:
            percent_increase = Shirt.size_price_increase[self.size.lower()]
            new_price = self.price + (self.price * percent_increase / 100)
            print(f"Price adjusted for size '{self.size}': {new_price}")
            self.price = new_price
        else:
            print("Invalid size entered. Price not adjusted.")

    def showShirt(self):
        print("\nShirt Details:")
        print(f"Shirt ID   : {self.sid}")
        print(f"Shirt Name : {self.sname}")
        print(f"Type       : {self.type}")
        print(f"Size       : {self.size}")
        print(f"Price      : {self.price}")

s1 = Shirt()  
s2 = Shirt(301, "Peter England", "Formal", 1000, "medium")
s3 = Shirt(302, "Allen Solly", "Casual", 1000, "xlarge")

s1.showShirt()
s2.showShirt()
s3.showShirt()

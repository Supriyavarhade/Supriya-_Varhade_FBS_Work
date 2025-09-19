class Shirt:
    def __init__(self, sid ="none", sname ="none", stype ="0", price ="0", size ="none"):
        self.sid = sid
        self.sname = sname
        self.type = stype
        self.price = price
        self.size = size

    def showShirt(self):
        print("sid:", self.sid)
        print("sname:", self.sname)
        print("stype:",self.type)
        print("size:",self.size)

    def __del__ (self):
        print("shirt object is destroyed")

s1 = Shirt("23" "sakshi", "formal", "small" )
s1.showShirt()
del s1

s2 = Shirt()
s2.showShirt()
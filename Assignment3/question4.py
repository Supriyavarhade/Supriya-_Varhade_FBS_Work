###iiput angles of a trangle and check whether tringle is valid or not

a = int(input("enter side1:"))
b = int(input("enter side2:"))
c = int(input("enter side3:"))

if(a + b > c and a + c > b and b +c > a):
    print("valid trangle")
else:
    print("not valid")
    

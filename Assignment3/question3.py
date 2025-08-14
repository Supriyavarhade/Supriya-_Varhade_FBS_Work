### input angles of a tringle is vowel or constant
a= int(input("input side1:"))
b = int(input("input side2:"))
c = int(input("input side3:"))

if(a+b>c and a+c>b and b+c>a):
    print("equilateral tringle")
else:
     print("scalene triangle.")
     
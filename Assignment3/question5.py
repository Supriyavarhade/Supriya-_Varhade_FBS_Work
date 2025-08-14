s1 = int(input("input side1:"))
s2 = int(input("input side2:"))
s3 = int(input("input side3:"))

if(s1 == s2 == s3):
    print("equilateral tringle")
elif(s1==s2 or s2==s3 or s1==s3):
     print("isosceles tringle:")
else:
     print("scalene triangle.")
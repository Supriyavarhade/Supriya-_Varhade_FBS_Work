### INPUT 5 SUBJECT MARKS FROM USER ID GRADE

m1 = int(input("enter the marks of sub1"))
m2 = int(input("enter the marks of sub1"))
m3 = int(input("enter the marks of sub1"))
m4 = int(input("enter the marks of sub1"))
m5 = int(input("enter the marks of sub1"))


total_marks = m1 +m2 + m3 + m4 + m5

average = total_marks / 5
print("average",average)

if(average >= 90):
    print("first class")
elif(average >= 70):
    print("second class")
elif(average >= 70):
    print("third class")
else:
    print("fail")
    


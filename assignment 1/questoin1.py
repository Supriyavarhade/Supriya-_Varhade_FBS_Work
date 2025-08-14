## write a program to calculate the percentage of student based on marks of 5 subject

m1=int(input("enter the marks of subject 1"))
m2=int(input("enter the marks of subject 2"))
m3=int(input("enter the marks of subject 3"))
m4=int(input("enter the marks of subject 4"))
m5=int(input("enter the marks of subject 5"))

gainmarks =m1 + m2 + m3 + m4 + m5

percentage =(gainmarks / 500)*100
print(f'total percentage of the student is: {percentage}%')
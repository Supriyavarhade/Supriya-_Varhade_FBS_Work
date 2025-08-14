### write a program to input two angles from user and find third angle of the triangle

a=int(input("enter the value of first angle:"))
b=int(input("enter the value of second angle:"))

third_angle = 180 -(a+b)
print(f'third angle is:{third_angle}')

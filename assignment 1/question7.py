#### write a program to find the roots of quadratic equation 

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))

sqrt =((b**2)-(4*a*c))
res1 =(-b+sqrt**0.5)/2*a
res2 =(-b-sqrt**0.5)/2*a
print(f'first root is:{res1}, second root is:{res2}')

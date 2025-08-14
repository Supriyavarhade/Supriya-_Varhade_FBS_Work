### write a program to enter p,t,r and calculate simple interest

p=int(input("enter the pricipal:"))
r=int(input("enter the interest:"))
t=int(input("enter the time(year):"))

simpleinterest=(p*r*t)/100
print(f'simple interest is:{simpleinterest}')
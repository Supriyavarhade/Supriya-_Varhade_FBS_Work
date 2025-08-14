### write a program to enter p,t,r and calculate compound interest

p = int(input("enter the pricipal amount:"))
r = int(input("enter the interest rate:"))
t = int(input("enter the time:"))

compound_int = (p*(1+r/100)**t)-p
print(f'compound interest is:{compound_int}')
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter a number: "))

print("Sum of 1 + 2 + ... + n is:", sum_natural(n))
print("Sum of 1! + 2! + ... + n! is:", sum_factorials(n))
print("Sum of 1^1 + 2^2 + ... + n^n is:", sum_powers(n))
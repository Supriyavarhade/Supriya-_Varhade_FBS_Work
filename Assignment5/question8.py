#a

n = int(input("Enter n: "))
sum_series = 0
fact = 1

for i in range(1, n+1):
    fact *= i
    sum_series += fact

print("Sum of series:", sum_series)


#b

N = int(input("Enter N: "))
sum_series = 0

for i in range(1, N+1):
    sum_series += N ** i

print("Sum of series:", sum_series)


#c
n = int(input("Enter n: "))
sum_series = 0

for i in range(n):
    sum_series += 2 ** i

print("Sum of geometric series:", sum_series)


#d
a = float(input("Enter a: "))
sum_series = 0

for i in range(1, 11):
    sum_series += (a ** i) / i

print("Sum of series:", sum_series)

#e
x = float(input("Enter value of x: "))
n_terms = int(input("Enter number of terms: "))
sum_e = 0
sign = 1
for k in range(1, n_terms + 1):
    denom = 2 * k - 1
    sum_e += sign * (x ** k) / denom
    sign *= -1
print("Sum :", sum_e)
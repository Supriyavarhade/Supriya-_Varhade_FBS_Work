def print_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


n = int(input("Enter how many terms: "))
print("Fibonacci series:")
print_fibonacci(n)
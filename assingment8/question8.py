def reverse_number(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return reverse

num = int(input("Enter a number: "))
print("Reverse of the number is:", reverse_number(num))
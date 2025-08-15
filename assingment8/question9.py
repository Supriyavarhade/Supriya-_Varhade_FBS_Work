def is_palindrome(number):
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return original == reverse

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
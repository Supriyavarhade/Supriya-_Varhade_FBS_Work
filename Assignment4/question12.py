num = int(input("enter a number:"))
original_num = num
sum = 0

while num> 0:
    digit = num%10
    sum += digit ** 3
    num = num // 10

if sum == original_num:
    print(f"{original_num} is an armstrong number")
else:
    print(f"{original_num} is not an armstrong number")
    
def is_armstrong(num):
    num_str = str(num)
    digits = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** digits
        
    return total == num


number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
### three digit number is pelindrone or not

num = int(input("enter number:"))

if num == int(str(num)[::-1]):
    print("it is palindrone.")
else:
    print("it is not palindrone.")


string = input("enter a non empty string:")
n = int(input("enter the index of the character to remove: "))
if n < 0 or n>= len(string):
    print("invalid index!")
else:
    new_string = string[:n] + string[n+1:]
    print("strig after removing charcter at index", n, ":", new_string)
    
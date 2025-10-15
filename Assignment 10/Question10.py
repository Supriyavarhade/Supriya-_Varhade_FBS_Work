list = [1, 2, 3, 4, 5, 6, 7 ,8]
num = int(input("Enter element to remove: "))
result = []
for i in list:
    if i != num:
        result.append(i)

print("list after removal:", result)
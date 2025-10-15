list = [1, 2, 3, 4, 5, 6]
new_list = []
for i in list:
    if i % 2 != 0:
        new_list.append(i)
print("after removing even numbers:", new_list)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("list after removing duplicates:", unique)

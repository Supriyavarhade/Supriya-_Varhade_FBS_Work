list = [10, 21, 30, 40, 50]
even = []
odd = []
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even list:", even)
print("odd list",odd)

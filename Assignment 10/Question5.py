nums = [1, 2, 3, 4, 5,]
x = int(input("Enter a number: "))
count = 0
for n in nums:
    if n == x:
        count += 1

if count > 0:
    print(x, "is present", count, "times")
else:
    print(x, "is not present in the list")
    
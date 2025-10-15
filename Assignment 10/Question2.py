nums = [1, 2, 3, 4, 5, 6]
maxi = nums[0]
mini = nums[0]

for n in nums:
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n


print("miximum:", maxi)
print("minimun:", mini)


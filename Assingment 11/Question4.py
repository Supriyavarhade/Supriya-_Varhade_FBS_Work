nums = [12, 13, 14, 15, 16]

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j+1],nums[j]

print("sorted list:", nums)
print("second list:",nums[-2])

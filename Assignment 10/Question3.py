nums = [12, 45, 7, 89, 23]
largest = second = -9999

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("second largest:", second)
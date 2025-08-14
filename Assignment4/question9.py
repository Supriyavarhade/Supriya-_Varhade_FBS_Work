start = int(input("start:"))
end = int(input("end:"))
div = int(input("divisor:"))

for i in range(start, end +1):
    if i % div == 0:
        print(i)
        
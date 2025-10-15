n = 100
rows = n// 10

for i in range(rows, 0, -1):
    start = (i-1)*10 + 1
    end = i * 10 + 1
    row = list(range(start, end))
    if i % 2 == 0:
        row.reverse()
        print(row)



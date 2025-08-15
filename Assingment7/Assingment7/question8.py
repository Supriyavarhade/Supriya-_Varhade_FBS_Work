rows = 5

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    spaces = (rows - i) * 2
    print("  " * spaces, end=" ")

    if i != rows:
        for j in range(i, 0, -1):
            print(j, end=" ")
    else:
        for j in range(i, 0, -1):
            print(j, end=" ")
    print()
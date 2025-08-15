amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum notes needed:")

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} : {count}")
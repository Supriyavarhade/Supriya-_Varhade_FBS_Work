n = int(input("Enter number of students: "))
percentages = []

for i in range(n):
    total = 0
    for j in range(5):
        marks = float(input(f"Enter marks for subject {j+1} of student {i+1}: "))
        total += marks
    percentages.append(total / 5)

for i in range(n):
    print(f"Student {i+1} Percentage: {percentages[i]:.2f}%")

print("Average Percentage:", sum(percentages) /n)
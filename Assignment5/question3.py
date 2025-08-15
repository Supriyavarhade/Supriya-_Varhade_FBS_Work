passenger = int(input("Enter number of passenger:"))
ticket_cost = float(input("Enter cost of ticket:"))

total_amount = 0

for i in range(1 , passenger + 1):
    age = int(input("Enter age:"))

if age < 12:
    fare = ticket_cost * 0.7
elif age > 59:
    fare = ticket_cost * 0.5
else:
    fare = ticket_cost

total_amount += fare

print(f'Ticket prize for all passengers:{total_amount}')
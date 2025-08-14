# ticket

ticket_amount = float(input("enter ticket amount per person:"))


for i in range(1,6):
    age = int(input("enter age of person:")) #+ str(1)

    if age < 12:
        discount = 0.30 * ticket_amount
    elif age > 59:
        discount = 0.50* ticket_amount

    else:
        discount = 0

        final_price = ticket_amount - discount
        total_amount += final_price

        print("total amount for 5 people:Rs.",round(total_amount,2))

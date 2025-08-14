### total electricity bill

units = float(input("enter total electricity units:"))
total_bill = 0

if(units > 0):
    if(units > 50):
        if(units > 150):
            if(units > 250):
                total_bill = 50* 0.5+ 100* 0.75+100*1.20
                units4 = units - 250
                total_bill = 50*0.5+100*0.75
            else:
                toatal_bill = 50*0.5 + 100 * 0.75
                units3 = units -150
                total_bill = total_bill + units + units3 * 1.50
        else:
            total_bill = 50*0.5
            unit2 = units-50
            total_length=total_bill +(unit2 * 0.75)
    else:
        total_bill=units*0.5
else:
    print("invalid input")

print(total_bill)

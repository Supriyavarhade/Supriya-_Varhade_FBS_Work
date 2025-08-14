### accept an integer amount from user and tell minimum number of notes needed for reprenting that amount

amount =int(input("enter the amount of minimum notes:"))

temp = amount

two_thousand = temp//2000
temp=temp%2000

five_hundread = temp//500
temp=temp%500

two_hundread =temp//200
temp = temp%200

fifty = temp//50
temp =temp%50

twenty = temp//20
temp=temp%20

ten = temp// 10
temp=temp% 10

total_notes=two_thousand + five_hundread + two_hundread + fifty +twenty + ten
print(f'total_notes:{total_notes}')
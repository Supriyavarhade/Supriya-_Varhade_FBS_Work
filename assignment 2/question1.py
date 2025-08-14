second = int(input("enter the seconds:"))
hours = second // 3600
second = second % 3600
min = second // 60
second = second % 60

print(f'hours{hours} , min{min} , second{second}')

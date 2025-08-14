import random

correct_userid = "admin"
correct_password = "1234"

userid = input("enter userid:")
password = input("enter password:")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000,9999)

    print(f'captcha:{captcha}')

    user_input = int(input("enter the captcha:"))

    if user_input == captcha:
        print("successful captcha matched:")
    else:
        print("failed captha did not match")

else:
    print("incorrect userid or password")
    
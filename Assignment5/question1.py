correct_userid = "admin"
correct_password = "1234"

for i in range(3):
    userid = input("Enter username:")
    password = input("Enter password:")
    if userid == correct_userid and password == correct_password:
        print("Login successfully")
        break
    else:
     print("Invalid credential! Please try again")
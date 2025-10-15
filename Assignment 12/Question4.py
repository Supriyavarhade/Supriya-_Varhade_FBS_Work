string = input(" Enter a string: ")
if len(string) < 2:
    print("new string: ", string)
else:
    new_string = string[-1] + string[1: -1] + string[0]
    print("new string:", new_string)

    
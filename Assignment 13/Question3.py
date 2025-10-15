d = {'name': 'supriya', 'age': 21, 'city': 'pune'}
key = input("Enter key to check: ")
if key in d:
    print(f"key '{key}' exists in the dictionary.")
else:
    print(f"key '{key}' does not exist.")
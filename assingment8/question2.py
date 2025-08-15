def calculate_area(radius):
    return 3.14 * radius ** 2


radius = float(input("Enter the radius of the circle: "))


area = calculate_area(radius)

print("The area of the circle is:", area)
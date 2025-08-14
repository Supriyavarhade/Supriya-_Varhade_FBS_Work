### convert distant given in feet and inches into meter and centimeter

feet=int(input("enter the feet:"))
inches=int(input("enter the inches:"))

total_meters=(feet*0.3048) + (inches*0.0254)

meters = int(total_meters)
centimeters=(total_meters - meters)*100
print("meters",meters)
print("centimeters",centimeters)
len_1 = float(input("Enter the length of the first rectangle: ")) #Get the dimentions of two rectangles
wid_1 = float(input("Enter the length of the first rectangle: "))
len_2 = float(input("Enter the length of the second rectangle: "))
wid_2 = float(input("Enter the width of the second rectangle: "))

area_1 = len_1 * wid_1 #Calculate area of rectangle 1
area_2 = len_2 * wid_2 #Calculate area of rectangle 2

if (area_1 > area_2):
	print("Rectangle 1 is larger.")
elif (area_2 > area_1):
	print("Rectangle 2 is larger.")
else:
	print("The rectangles are the same size.")	
user_value = int(input("Enter a value between zero and eight: "))

if (user_value > 0) and (user_value < 8):
	if (user_value == 1):
		print("Monday")
	elif (user_value == 2):
		print("Tuesday")
	elif (user_value == 3):
		print("Wednesday")
	elif (user_value == 4):
		print("Thursday")
	elif (user_value == 5):
		print("Friday")
	elif (user_value == 6):
		print("Saturday")
	elif (user_value == 7):
		print("Sunday")
else:
	print("Error. Value out of range")
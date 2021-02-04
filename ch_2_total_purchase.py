item_1 = float(input("What is the price of your first item? "))
item_2 = float(input("What is the price of your second item? "))
item_3 = float(input("What is the price of your third item? "))
item_4 = float(input("What is the price of your fourth item? "))
item_5 = float(input("What is the price of your fifth item? "))

TAX = 1.07
subtotal = item_1 + item_2 + item_3 + item_4 + item_5

print("Your subtotal is $", format(subtotal, ',.2f'), ".")
print("Tax is 7%.")
total = subtotal * TAX
print("Your total is $", format(total, ',.2f')) 


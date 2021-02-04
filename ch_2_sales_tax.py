purchase = float(input("Enter the purchase total: "))

state_tax = purchase * 0.05
country_tax = purchase * 0.025 
total_tax = state_tax + country_tax
total = purchase + total_tax

print("Purchase: $", format(purchase, ',.2f'), sep='')
print("State tax: $", format(state_tax, ',.2f'), sep='')
print("County tax: $", format(country_tax, ',.2f'), sep='')
print("Total tax: $", format(total_tax, ',.2f'), sep='')
print("Your total is: $", format(total, ',.2f'), sep='')


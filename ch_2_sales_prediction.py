sales = float(input("Enter projected sales: "))

SALES_PERCENT = 0.23

projected_profit = sales * SALES_PERCENT

print("The profit will be $", format(projected_profit, ',.2f'), ".", sep='')

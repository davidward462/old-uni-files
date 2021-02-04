def getCosts():
	print("Monthly costs")
	loanPayment = float(input("  Enter loan payment: "))
	insurance = float(input("  Enter insurance: "))
	gasCost = float(input("  Enter gas cost: "))
	oilCost= float(input("  Enter oil cost: "))
	tirePayment = float(input("  Enter tire payment: "))
	maintenanceCost = float(input("  Enter maintenance cost: "))
	return loanPayment, insurance, gasCost, oilCost, tirePayment, maintenanceCost

def main():
	loanPayment, insurance, gasCost, oilCost, tirePayment, maintenanceCost = getCosts()
	
	monthlyTotal = loanPayment+ insurance+ gasCost+ oilCost+ tirePayment+ maintenanceCost
	print("\nMonthly total: $%.2f" % monthlyTotal)
	yearlyCosts = monthlyTotal * 12
	print("Yearly costs: $%.2f" % yearlyCosts)

main()


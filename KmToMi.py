def convert(km):
	return km * 0.6214


def main():
	km = float(input("Enter km: "))
	mi = convert(km)
	
	print("%.2f kilometers is %.2f miles." % (km, mi))

main()
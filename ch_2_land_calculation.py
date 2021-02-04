FT_SQ_PER_ACRE = 43560

area_ft_sq = float(input("Enter the area in square feet: "))

area_acre = area_ft_sq / FT_SQ_PER_ACRE

print("Your property is", format(area_acre, ',.2f'), "acres.")
meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

tip = meal_cost*tip_percent*.01
tax = meal_cost*tax_percent*.01
tc = round(meal_cost + tip + tax)

print(tc)

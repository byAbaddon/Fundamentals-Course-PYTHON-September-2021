budget = float(input())
kg_fl = float(input())

coz_count = 0
eggs_count = 0

egg_price = kg_fl * 0.75
milk_price = kg_fl * 1.25 / 4
coz_sum_one = kg_fl + egg_price + milk_price

loop = 0

while budget > coz_sum_one:

    budget -= coz_sum_one
    coz_count += 1
    eggs_count += 3
    loop += 1

    if loop == 3:
        eggs_count -= coz_count - 2
        loop = 0

print(f'You made {coz_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')

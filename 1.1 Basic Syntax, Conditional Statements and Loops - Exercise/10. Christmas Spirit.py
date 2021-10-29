quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
budget = 0
totalSpirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 10 == 0:
        totalSpirit -= 20
        budget += tree_skirt + tree_lights + tree_garlands

        if day == days:
            totalSpirit -= 30

    if day % 5 == 0:
        totalSpirit += 17
        budget += tree_lights * quantity

    if day % 15 == 0:
        totalSpirit += 30

    if day % 3 == 0:
        totalSpirit += 13
        budget += (tree_garlands + tree_skirt) * quantity

    if day % 2 == 0:
        totalSpirit += 5
        budget += ornament_set * quantity

print(f'Total cost: {budget}\nTotal spirit: {totalSpirit}')

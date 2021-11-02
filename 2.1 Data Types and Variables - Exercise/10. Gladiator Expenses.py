lost_fight, helmet, sword, shield, armor = [float(input()) for _ in range(5)]
count_broken_shield = money = 0

for day in range(1, int(lost_fight) + 1):
    if day % 2 == 0:
        money += helmet
    if day % 3 == 0:
        money += sword
    if day % 2 == 0 and day % 3 == 0:
        money += shield
        count_broken_shield += 1
        if count_broken_shield == 2:
            money += armor
            count_broken_shield = 0

print(f'Gladiator expenses: {money:.2f} aureus')


'''
7
2
3
4
5

output: Gladiator expenses: 608.00 aureus
'''
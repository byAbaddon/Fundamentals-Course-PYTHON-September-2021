input_list = input().split('|')
energy, coins = 100, 100

while input_list:
    current = input_list.pop(0).split('-')
    event = current[0]
    num = int(current[1])

    if event == 'rest':
        if energy == 100:
            print(f'You gained {0} energy.\nCurrent energy: {100}.')
            energy = 100
        elif energy + num > 100:
            print(f'You gained {energy + num - 100} energy.\nCurrent energy: {100}.')
        else:
            energy += num
            print(f'You gained {num} energy.\nCurrent energy: {energy}.')

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += num
            print(f'You earned {num} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - num > 0:
            coins -= num
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            exit()

print(f'Day completed!\nCoins: {abs(coins)}\nEnergy: {energy}')

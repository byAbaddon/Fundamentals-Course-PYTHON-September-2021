size = int(input())
all_days = int(input())
coins = 0

for days in range(1, all_days + 1):
    if days % 10 == 0:
        size -= 2
    if days % 15 == 0:
        size += 5

    coins += 50
    coins -= size * 2

    if days % 3 == 0:
        coins -= size * 3
    if days % 5 == 0:
        coins += size * 20
        if days % 3 == 0:
            coins -= size * 2

print(f'{size} companions received {coins // size} coins each.')

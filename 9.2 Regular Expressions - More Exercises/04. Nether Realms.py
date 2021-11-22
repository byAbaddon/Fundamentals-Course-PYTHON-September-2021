import re

data = re.split('[, ]+', input())
data = list(sorted(data))
regex_char = r'[^0-9\s.\/+*-]'
regex_num = r'(-?\d*\.?\d+)'

while data:
    health = 0
    damage = 0
    demon = data.pop(0)

    match_char = re.findall(regex_char, demon)
    for el in match_char:
        health += ord(el)

    match_num = re.findall(regex_num, demon)

    damage = sum(map(float, match_num))
    for i in range(len(demon)):
        if demon[i] == '*':
            damage *= 2
        elif demon[i] == '/':
            damage /= 2

    print(f"{demon.strip()} - {health} health, {damage:.2f} damage")


'''
M3ph-0.5s-0.5t0.0**

-------------------------output:
M3ph-0.5s-0.5t0.0** - 524 health, 8.00 damage
'''
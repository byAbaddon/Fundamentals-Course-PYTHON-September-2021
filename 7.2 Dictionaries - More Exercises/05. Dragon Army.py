catalog_dragons = {}  # color {name : {'damage':damage, 'health': health, 'armor': armor}}

for _ in range(int(input())):
    color, name, damage, health, armor = [int(x) if x.isdigit() else x for x in input().split()]
    damage = 45 if damage == 'null' else damage
    health = 250 if health == 'null' else health
    armor = 10 if armor == 'null' else armor

    if color not in catalog_dragons:
        catalog_dragons[color] = {}
        catalog_dragons[color][name] = {'damage': damage, 'health': health, 'armor': armor}
    else:
        if name in catalog_dragons[color]:
            catalog_dragons[color][name] = {'damage': damage, 'health': health, 'armor': armor}
        else:
            catalog_dragons[color][name] = {'damage': damage, 'health': health, 'armor': armor}

for key, val in catalog_dragons.items():
    d_avg = sum([catalog_dragons[key][index]['damage'] for index, k in catalog_dragons[key].items()]) / len(val)
    h_avg = sum([catalog_dragons[key][index]['health'] for index, k in catalog_dragons[key].items()]) / len(val)
    a_avg = sum([catalog_dragons[key][index]['armor'] for index, k in catalog_dragons[key].items()]) / len(val)

    print(f'{key}::({d_avg:.2f}/{h_avg:.2f}/{a_avg:.2f})')
    sort = dict(sorted(catalog_dragons[key].items()))
    for k, v in sort.items():
        print(f'-{k} -> damage: {v["damage"]}, health: {v["health"]}, armor: {v["armor"]}')

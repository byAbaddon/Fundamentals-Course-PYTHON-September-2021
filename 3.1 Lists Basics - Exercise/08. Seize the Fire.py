fires = input().split('#')
water = int(input())

coll_list = []
effort = 0

type_fires = {
    'High': {'Min': 81, 'Max': 125},
    'Medium': {'Min': 51, 'Max': 80},
    'Low': {'Min': 1, 'Max': 50},
}

while len(fires) > 0:
    level, lt_water = fires.pop(0).split(' = ')

    if type_fires[level]:
        mn = type_fires[level]['Min']
        mx = type_fires[level]['Max']

        if mn <= int(lt_water) <= mx and water >= int(lt_water):
            coll_list.append(int(lt_water))
            water -= int(lt_water)
            effort += int(lt_water) * 0.25

print('Cells:')
for i in range(len(coll_list)):
    print('-', coll_list[i])
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(coll_list)}')


'''
High = 89#Low = 28#Medium = 77#Low = 23
1250

------------------output:
Cells:
- 89
- 28
- 77
- 23
Effort: 54.25
Total Fire: 217
'''
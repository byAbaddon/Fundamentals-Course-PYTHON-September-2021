import os
os.system('clear')
#------------------------------copy/paste------------------------------------
animalList = []
animalInfo = []
zoneName = []
zoneInfo = []

while True:
    command = input()
    if command == 'Last Info':
        break
    else:
        commandSplit = command.split(':')
        subCom = commandSplit[0]
        animalName = commandSplit[1]
        animalFood = int(commandSplit[2])
        animalArea = commandSplit[3]
        if subCom == 'Add':
            if animalName not in animalList:
                animalList.append(animalName)
                animalInfo.append([animalName, animalFood, animalArea])
                if animalArea not in zoneName:
                    zoneName.append(animalArea)
                    zoneInfo.append([1, animalArea])
                else:
                    zoneIndex = zoneName.index(animalArea)
                    zoneInfo[zoneIndex][0] += 1
            else:
                animalIndex = animalList.index(animalName)
                animalInfo[animalIndex][1] += animalFood
        elif subCom == 'Feed':
            if animalName in animalList:
                animalIndex = animalList.index(animalName)
                animalInfo[animalIndex][1] -= animalFood
                if animalInfo[animalIndex][1] <= 0:
                    print(f"{animalName} was successfully fed")
                    animalList.pop(animalIndex)
                    animalInfo.pop(animalIndex)
                    zoneIndex = zoneName.index(animalArea)
                    zoneInfo[zoneIndex][0] -= 1
                    if zoneInfo[zoneIndex][0] == 0:
                        zoneInfo.pop(zoneIndex)
                        zoneName.pop(zoneIndex)

print("Animals:")
sortedAnimalInfo = sorted(animalInfo, key=lambda x: (-x[1], x[0]))
for index, value in enumerate(sortedAnimalInfo):
    print(f"{value[0]} -> {value[1]}g")
sortedZoneList = sorted(zoneInfo, key=lambda x: -x[0])
print("Areas with hungry animals:")
for i in sortedZoneList:
    print(f"{i[1]} : {i[0]}")




#---------------------------------TODO


from collections import Counter

animals = {}

while True:
    current = input().split(':')
    if current[0] == 'Last Info':
        break

    command = current[0]
    name = current[1]
    food = int(current[2])
    area = current[3]

    if command == 'Add':
        if name not in animals:
            animals[name] = {'food' : food, 'area' : area}
        else:    
            animals[name]['food'] += food
    elif command == 'Feed':
        if name in animals:
            animals[name]['food'] -= food
            if animals[name]['food'] <= 0:
                print(f'{name} was successfully fed')
                del animals[name]


counter = Counter()
sort_animals_by_food = dict(sorted(animals.items(), key = lambda x : x[1]['food'], reverse=True))

print('Animals:')

for k,v in sort_animals_by_food.items():
    print(f"{k} -> {v['food']}g")
    count = v['area']
    counter[count] += 1

sort_area_by_name = dict(sorted(counter.items(), key=lambda x : x[0] , reverse=True))

print('Areas with hungry animals:')

for k,v in sort_area_by_name.items():
    print(f'{k} : {v}')




'''

Add:Bonie:3490:RiverArea
Add:Sam:5430:DeepWoodsArea
Add:Bonie:200:RiverArea
Add:Maya:4560:ByTheCreek
Feed:Maya:2390:ByTheCreek
Feed:Bonie:3500:RiverArea
Feed:Johny:3400:WaterFall
Feed:Sam:5500:DeepWoodsArea
Last Info

'''
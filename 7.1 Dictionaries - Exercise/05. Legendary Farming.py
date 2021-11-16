legend = {'Shards': 'Shadowmourne', 'Fragments': 'Valanyr', 'Motes': 'Dragonwrath'}
materials = {'Shards': 0, 'Fragments': 0, 'Motes': 0}
junk = {}

while True:
    data = input().title().split()
    for i in range(0, len(data), 2):
        val = int(data[i])
        key = data[i + 1]

        if key not in legend:
            if key not in junk:
                junk[key] = 0

            junk[key] += val
            continue
        else:
            materials[key] += val

        if materials[key] >= 250:
            materials[key] -= 250
            sorted_materials = dict(sorted(materials.items(), key=lambda x: (-x[1], x[0])))
            sorted_junk = dict(sorted(junk.items()))

            print(legend[key], 'obtained!')

            for k, v in sorted_materials.items():
                print(f'{k.lower()}: {v}')

            for k, v in sorted_junk.items():
                print(f'{k.lower()}: {v}')

            exit()

'''
3 Motes 5 stones 5 Shards
6 leathers 255 fragments 7 Shards
'''

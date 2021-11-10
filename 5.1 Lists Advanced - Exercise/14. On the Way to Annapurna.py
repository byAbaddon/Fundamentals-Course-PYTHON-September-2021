stores = {}

while True:
    token = input().split('->')
 
    if token[0] == 'END':
        break
    elif token[0] == 'Add':
        items = [item for item in token[2].split(',')]
        if token[1] not in stores:
            stores[token[1]] = items
        else:
            stores[token[1]] += items
    elif token[0] == 'Remove':
        if token[1] in stores:
            del stores[token[1]]

sort_stores = dict(sorted(stores.items(), key=lambda x: (len(x[1]) , x[0]), reverse=True))

print('Stores list:')
for k, v in sort_stores.items():
    print(k)
    for el in v:
        print('<<' + el + '>>')

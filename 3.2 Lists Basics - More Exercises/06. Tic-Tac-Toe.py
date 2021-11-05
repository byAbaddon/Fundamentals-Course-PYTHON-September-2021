arr = [input().split() for _ in range(3)]
union = arr[0] + arr[1] + arr[2]
result = list()

# horizontal test
result.append((len(set(union[0:3])) == 1, union[0]))
result.append((len(set(union[3:6])) == 1, union[3]))
result.append((len(set(union[6:9])) == 1, union[6]))

# vertical test
result.append((len(set(union[0:9:3])) == 1, union[0]))
result.append((len(set(union[1:9:3])) == 1, union[1]))
result.append((len(set(union[2:9:3])) == 1, union[2]))

# diagonal test
result.append((len(set(union[0:9:4])) == 1, union[0]))
result.append((len(set(union[2:8:2])) == 1, union[2]))

for index in result:
    if index[0]:
        if index[1] == '1':
            print('First player won')
            exit()
        elif index[1] == '2':
            print('Second player won')
            exit()

print('Draw!')

arr = list(map(int, input().split(', ')))
group = 10

while arr:
    current = list(filter(lambda x: x <= group, arr))
    arr = list(filter(lambda x: x > group, arr))
    print(f'Group of {group}\'s:', current)

    group += 10

# 8, 12, 38, 3, 17, 19, 25, 35, 50

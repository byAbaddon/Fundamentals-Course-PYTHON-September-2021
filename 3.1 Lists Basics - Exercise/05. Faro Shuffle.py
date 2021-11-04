str_list = input().split(' ')
faro = int(input())

first = []
second = []

for _ in range(faro):
    for i in range(len(str_list)):
        if i < len(str_list) // 2:
            first.append(str_list[i])  # 1 2 3
        else:
            second.append(str_list[i])  # 4 5 6

    str_list.clear()

    for j in range(0, len(first)):
        str_list.append(first[j])
        str_list.append(second[j])  # 1 2 3 4 5 6

    first.clear()
    second.clear()

print(str_list)

'''
1 2 3 4 5 6
2
'''

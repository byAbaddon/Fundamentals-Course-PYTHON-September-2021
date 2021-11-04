coll_list = input().split(', ')
beggars = int(input())
beggars_list = [0] * beggars

for i in range(len(coll_list)):
    beggars_list[i % beggars] += int(coll_list[i])

print(beggars_list)


'''
1, 2, 3, 4, 5
2
'''
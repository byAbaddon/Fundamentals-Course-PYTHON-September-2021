num_list = input().split(', ')
count_zeros = num_list.count('0')
print([int(x) for x in num_list if x != '0'] + [0] * count_zeros)


# --------------------------------------------------------(2)----------------------
# coll_list = list(map(int, input().split(', ')))
# a = [int(x) for x in coll_list if int(x) != 0]
# b = [int(z) for z in coll_list if int(z) == 0]
# print(a + b)


'''
1, 0, 1, 2, 0, 1, 3

output: [1, 1, 2, 1, 3, 0, 0]
'''

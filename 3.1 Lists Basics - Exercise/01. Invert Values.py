print([abs(int(x)) if int(x) < 0 else int(x) * -1 for x in input().split()])

# ----------------------------(2)-------------------------------------------
# num_list = list(map(int, input().split(' ')))
# filter_list = list(map(lambda x: x * -1 if x > 0 else abs(x), num_list))
#
# print(filter_list)

'''
 1 2 -3 -3 5
 output: [-1, -2, 3, 3, -5]
'''

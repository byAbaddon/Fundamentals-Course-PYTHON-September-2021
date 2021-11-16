string = input()
char_set = sorted(set(x for x in string if not x == ' '), key=string.index)
[print(f'{x} -> {string.count(x)}') for x in char_set]


# -------------------------------------(2)--------------------------
# count_dict = {}
#
# for char in input():
#     if char not in count_dict:
#         count_dict[char] = 0
#     count_dict[char] += 1
#
# [print(k, '->', v) for k, v in count_dict.items() if k != ' ']


'''
text
---------------
output:
t -> 2
e -> 1
x -> 1

'''
from math import sqrt, floor

x1, y1, x2, y2 = [floor(float(input())) for _ in range(4)]


def calc(x, y):
    return sqrt(x ** 2 + y ** 2)


print(f'{x1, y1}' if calc(x1, y1) <= calc(x2, y2) else f'{x2, y2}')

'''
2
4
-1
2

output: (-1, 2)
'''
# ----------------------------------------(2)---------------------------------
# from math import sqrt, floor
#
# x1, y1, x2, y2 = [floor(float(input())) for _ in range(4)]
# first_dist = sqrt(x1 ** 2 + y1 ** 2)
# second_dist = sqrt(x2 ** 2 + y2 ** 2)
#
# if first_dist >= second_dist:
#     result = x2, y2
# else:
#     result = x1, y1
#
# print(result)






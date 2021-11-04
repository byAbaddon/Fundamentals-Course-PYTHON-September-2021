gifts_list = input().split()
while True:
    com, *args = input().split()
    if com == 'No': break
    if com == 'OutOfStock':
        gifts_list = [None if x == args[0] else x for x in gifts_list]
    if com == 'Required' and len(gifts_list) > int(args[1]) >= 0:
        gifts_list[int(args[1])] = args[0]
    if com == 'JustInCase':
        gifts_list[-1] = args[0]

print(*[x for x in gifts_list if x is not None])

# ------------------------------------------------------(2)-------------------

# gifts_list = list(input().split(' '))
#
# while True:
#     current = input().split(' ')
#     if len(current) == 2:
#         com, gift = current[0], current[1]
#     else:
#         com, gift, index = current[0], current[1], int(current[2])
#
#     if com == 'No':
#         break
#
#     elif com == 'OutOfStock':
#         gifts_list = list(map(lambda x: None if x == gift else x, gifts_list))
#     elif com == 'Required':
#         if len(gifts_list) - 1 >= index >= 0:
#             gifts_list[index] = gift
#
#     elif com == 'JustInCase':
#         gifts_list[-1] = gift
#
# print(*filter(lambda x: x is not None, gifts_list))


'''
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money

-----------------output:
StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg

'''

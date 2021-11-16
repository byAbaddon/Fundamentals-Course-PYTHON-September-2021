miner_dict = {}

while True:
    key = input()
    if key == 'stop':
        [print(k, '->', v) for k, v in miner_dict.items()]
        break
    else:
        val = int(input())
        if key not in miner_dict.keys():
            miner_dict[key] = 0
        miner_dict[key] += val

#   ---------------(2)------------------------


# count_dict = {}
#
# while True:
#     key = input()
#     if key == 'stop':
#         break
#     val = int(input())
#     if key not in count_dict:
#         count_dict[key] = 0
#     count_dict[key] += val
#
# [print(k, '->', v) for k, v in count_dict.items() if k != ' ']


'''
gold
155
silver
10
copper
17
gold
15
stop
----------------
output:
gold -> 170
silver -> 10
copper -> 17
'''

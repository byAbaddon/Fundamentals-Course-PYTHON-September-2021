coll_list = [int(input()) for _ in range(int(input()))]
command = input()

options_dict = {
    'even': [x for x in coll_list if not x & 1],
    'odd': [x for x in coll_list if x & 1],
    'negative': list(filter(lambda x: x < 0, coll_list)),
    'positive': list(filter(lambda x: x >= 0, coll_list)),
}

print(options_dict[command])

'''
5
33
19
-2
18
998
even
'''

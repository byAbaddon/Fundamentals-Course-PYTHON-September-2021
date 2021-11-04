loop, searching_word = int(input()), input()
words_list = [input() for _ in range(loop)]
match_list = [x for x in words_list if searching_word in x]
print(f'{words_list}\n{match_list}')

'''
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni
'''
# -----------------------------------(2)---------------------------
# n = int(input())
# word = input()
#
# coll_list = [input() for _ in range(n)]
# filtered_list = list(filter(lambda string: word in string, coll_list))
#
# print(coll_list)
# print(filtered_list)

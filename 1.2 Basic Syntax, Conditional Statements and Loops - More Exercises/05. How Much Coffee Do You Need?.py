catalog_list = [x for x in iter(input, 'END')]
words_list = ['coding', 'dog', 'cat', 'movie']
count = 0

for word in words_list:
    if word in catalog_list:
        count += 1
    if word.upper() in catalog_list:
        count += 2

print('You need extra sleep' if count > 5 else count)


'''
dog
CAT
gaming
END

output: 3
'''
# -----------------------------------(2)------------------------------------
# entry = input()
# obj = {'coding': 0, 'CODING': 0, 'movie': 0, 'MOVIE': 0, 'dog': 0, 'DOG': 0, 'cat': 0, 'CAT': 0, 'count': 0}
# counter = 0
#
# while entry != 'END':
#     obj['count'] += 1
#
#     if entry in obj:
#         if entry.isupper():
#             obj[entry] += 2
#             counter += 2
#         else:
#             obj[entry] += 1
#             counter += 1
#
#     entry = input()
#
# if counter > 5:
#     print('You need extra sleep')
# else:
#     print(counter)

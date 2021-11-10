matches, words = [input().split(', ') for i in range(2)]
print([match if match in words else None for match in matches for word in words if match in word])
# --------------------------------------(2)--------------------
# chars, words, unique = input().split(", "), input().split(", "), []
# [unique.append(char) if char not in unique else None for char in chars for word in words if char in word]
# print(unique)

# --------------------------------------(3)---------------------
# find_words = input().split(', ')
# arr = input().split(', ')
# unique = []
#
# for word in find_words:
#     for match in arr:
#         if word in match:
#             None if word in unique else unique.append(word)
#
# print(unique)

'''
arp, live, strong
lively, alive, harp, sharp, armstrong

output: ['arp', 'live', 'strong']
'''

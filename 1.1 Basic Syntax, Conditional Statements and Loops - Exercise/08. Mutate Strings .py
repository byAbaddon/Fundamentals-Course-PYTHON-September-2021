word, re_word = input(), input()
[print(re_word[:i + 1] + word[i + 1:]) for i in range(len(word)) if word[i] != re_word[i]]


# --------------------------------(2)------------------------

# word = input()
# re_word = input()
# collection = ''

# for i in range(len(word)):
#     if word[i] != re_word[i]:
#         collection = re_word[0:i + 1] + word[i + 1:100]
#         print(collection)

'''
Kitty
Doggy
'''


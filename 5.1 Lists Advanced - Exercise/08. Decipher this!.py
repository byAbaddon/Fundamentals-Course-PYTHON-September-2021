import re

arr = input().split()
decripted_word = []
while arr:
    word = arr.pop(0)
    num = list(filter(lambda x: x != '', re.split('\D+', word)))
    string = list(filter(lambda x: x != '', re.split('\d', word)))

    start_char = chr(int(num[0]))
    if len(string[0]) > 1:
        f_char = string[0][0:1]
        l_char = string[0][-1]
        decripted_word.append(start_char + l_char + string[0][1:-1] + f_char)
    else:
        decripted_word.append(start_char + string[0])

print(*decripted_word)


# -------------------------------------------------(2)------------------

# arr = input().split()
# decripted_word = []
#
# while arr:
#     word = arr.pop(0)
#     start_char = ''.join(list(filter(lambda x: x.isdigit(), word)))
#     string = word[len(start_char):]
#     start_char = chr(int(start_char))
#
#     if len(string) > 1:
#         f_char = string[0:1]
#         l_char = string[-1]
#         decripted_word.append(start_char + l_char + string[1:-1] + f_char)
#     else:
#         decripted_word.append(start_char + string)
#
# print(*decripted_word)




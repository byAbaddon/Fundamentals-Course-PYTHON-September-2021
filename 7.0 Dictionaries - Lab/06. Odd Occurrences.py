input_list = input().lower().split()
data_dict = {}
for word in input_list:
    if not data_dict.get(word):
        data_dict[word] = 1
    else:
        data_dict[word] += 1

for k, v in data_dict.items():
    if v & 1:
        print(k, end=' ')


# -----------------------------------------(2)----------------------------

# input_list = input().lower().split()
# data = {}
#
#
# def isOdd(word):
#     result = input_list.count(word)
#     if result & 1:
#         data[word] = 1
#         return data
#
#
# for word in input_list:
#     isOdd(word)
#
# print(*data)

'''
Java C# PHP PHP JAVA C java
---------------------------
output:  java c# c
'''
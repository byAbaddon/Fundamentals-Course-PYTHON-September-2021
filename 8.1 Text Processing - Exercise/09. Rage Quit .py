data = input().upper()
collection, current, sum_digits = '', '', ''
index = 0

while True:
    try:
        if not data[index].isdigit():
            current += data[index]
            index += 1
        else:
            for j in range(index, len(data)):
                if not data[j].isdigit():
                    break
                else:
                    sum_digits += str(data[j])
                    index += 1
            collection += current * int(sum_digits)
            current, sum_digits = '', ''
    except:
        break

print(f'Unique symbols used: {len(set(collection))}')
print(collection)

# ---------------------------------------------------(2)---------------------------------------------

# text = input().upper()
# result, num_str, num = '', '', ''
# index, start_index, next_index = 0, 0, 0


# while index < len(text):

#     if text[index].isdigit():     
#         num_str = text[index]
#         next_index = 1    

#         if index + 1 < len(text) and text[index + 1].isdigit():
#             num_str += text[index +1]
#             next_index = 2

#         num = int(num_str)
#         result += text[start_index: index] * num

#         if index + 1 >= len(text):
#             break

#         start_index = index + next_index

#     index += 1

# print(f'Unique symbols used: {len(set(result))}\n{result}')


'''
aSd2&5s@1
----------output:

Unique symbols used: 5
ASDASD&&&&&S@
'''
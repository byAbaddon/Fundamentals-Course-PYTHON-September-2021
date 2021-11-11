text = []
numbers_list = []
result = []

for char in input():
    numbers_list.append(int(char)) if char.isdigit() else text.append(char)

for i in range(len(numbers_list)):
    if not i & 1:
        if numbers_list[i] != 0:  # take
            result += (text[0: numbers_list[i]])
            text = text[numbers_list[i]:]
    else:  # skip
        text = text[numbers_list[i]:]

print(''.join(result))

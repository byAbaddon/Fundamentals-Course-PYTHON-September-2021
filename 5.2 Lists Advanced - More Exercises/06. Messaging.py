num = input().split(' ')
text = input()

calc_index = 0
result = ''

for i in range(len(num)):
    for digit in num[i]:
        calc_index += int(digit)
    current_index = calc_index - len(text)
    result += text[current_index]
    text = text[:current_index] + text [current_index + 1:]
    calc_index = 0

print(result)  

      


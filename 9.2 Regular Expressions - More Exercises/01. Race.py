import re

name_list = {x: x if x is None else 0 for x in input().split(', ')}
regex_char = r'(?P<char>[A-Za-z])'
regex_digit = r'(?P<digit>\d)'

while True:
    text = input()
    if text == 'end of race':
        break
    result_char = re.findall(regex_char, text)
    result_digit = re.findall(regex_digit, text)

    name = ''.join(result_char)
    sum_km = sum(map(int, (result_digit)))

    if name in name_list:
        name_list[name] += sum_km

sort_name_list = dict(sorted(name_list.items(), key=lambda x: -x[1]))
index = 1

for key in sort_name_list:
    if index < 4:
        position = ['st', 'nd', 'rd']
        print(f'{index}{position[index - 1]} place: {key}')
    index += 1



'''
George, Peter, Bill, Tom
G4e@55or%6g6!68e!!@
R1@!3a$y4456@
B5@i@#123ll
G@e54o$r6ge#
7P%et^#e5346r
T$o553m&6
end of race

------------------------output:
1st place: George
2nd place: Peter
3rd place: Tom
'''



import re

attacked_planet_dict = {}
destroyed_planet_dict = {}
count_Attack_planet = 0
count_destroyed_planet = 0

for _ in range(int(input())):
    text = input()
    decoding_message = ''
    code_regex = r"[star]"
    matches = re.findall(code_regex, text, re.IGNORECASE)

    for char in text:
        decoding_message += chr(ord(char) - len(matches))

    regex = r"@(?P<Planet>[A-za-z]+)\d*[^@\-!:>]*:(?P<Population>\d+)[^@\-!:>]*!(?P<Action>[AD])![^@\-!:>]*->(?P<Soldier>\d+)"

    result = re.finditer(regex, decoding_message)
    for el in result:
        if el.group('Action') == 'A':
            count_Attack_planet += 1
            attacked_planet_dict[el.group('Planet')] = el.group('Action')
        else:
            count_destroyed_planet += 1
            destroyed_planet_dict[el.group('Planet')] = el.group('Action')

sort_attacked_planet_dict = dict(sorted(attacked_planet_dict.items()))
sort_destroyed_planet_dict = dict(sorted(destroyed_planet_dict.items()))

print('Attacked planets:', count_Attack_planet)
for k in sort_attacked_planet_dict:
    print('->', k)

print('Destroyed planets:', count_destroyed_planet)
for k in sort_destroyed_planet_dict:
    print('->', k)

'''
2
STCDoghudd4=63333$D$0A53333
EHfsytsnhf?8555&I&2C9555SR

------------------------------output:
Attacked planets: 1
-> Alderaa
Destroyed planets: 1
-> Cantonica
'''
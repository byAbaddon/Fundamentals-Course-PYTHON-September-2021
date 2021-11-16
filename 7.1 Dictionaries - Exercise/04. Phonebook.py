phonebook_dict = {}
while True:
    token = input().split('-')
    if not len(token) == 1:
        key, val = token
        phonebook_dict[key] = val
    else:
        for _ in range(int(token[0])):
            name = input()
            if name in phonebook_dict:
                print(f'{name} -> {phonebook_dict[name]}')
            else:
                print(f'Contact {name} does not exist.')
        break



'''
Adam-0888080808
2
Mery
Adam
-----------------

output:
Contact Mery does not exist.
Adam -> 0888080808
'''

data = input().split(', ')

for word in data:
    if 3 <= len(word) <= 16:
        result = ''
        validation = True
        for char in word:
            if char.isalpha() or char.isdigit() or char == '-' or char == '_':
                result += char
            else:
                validation = False
                break
        if validation:
            print(result)

'''
sh, too_long_username, !lleg@l ch@rs, jeffbutt
-------- output:
jeffbutt
'''

students_obj = {}

while True:
    token = input()
    if not token.islower():
        name, id_num, course = token.split(':')
        students_obj[id_num] = {course: name}
    else:
        if 'basics' in token:
            token = token.split('_')
            token = token[0] + ' ' + token[1]
        for k, v in students_obj.items():
            if v.get(token):
                print(f'{v[token]} - {k}')
        break


'''
Peter:123:programming basics
John:5622:fundamentals
Maya:89:fundamentals
Lilly:633:fundamentals
fundamentals
-------------------
output:
John - 5622
Maya - 89
Lilly - 633

'''




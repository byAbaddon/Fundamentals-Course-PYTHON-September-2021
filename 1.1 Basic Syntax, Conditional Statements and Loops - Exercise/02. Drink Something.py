num = int(input())
result = ''

if num <= 14:
    result = 'drink toddy'
elif 14 < num <= 18:
    result = 'drink coke'
elif 18 < num <= 21:
    result = 'drink beer'
elif num > 21:
    result = 'drink whisky'

print(result)


'''
13
output: drink toddy
'''

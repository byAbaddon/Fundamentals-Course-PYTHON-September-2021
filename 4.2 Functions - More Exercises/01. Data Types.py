data_obj = {'int': lambda x: int(x) * 2,
            'real': lambda x: f'{(float(x) * 1.5):.2f}',
            'string': lambda x: f'${x}$'
            }

print(data_obj[input()](input()))

'''
int
5
output: 10
'''

# ----------------------------------------(2)--------------------------
# def data():
#     command, el = input(), input()
#     data_obj = {'int': lambda x: int(x) * 2,
#                 'real': lambda x: f'{(float(x) * 1.5):.2f}',
#                 'string': lambda x: f'${x}$'
#                 }
#
#     return data_obj[command](el)
#
#
# print(data())
# -----------------------------------------(3)---------------------

# arg, el = input(), input()
#
# if arg == 'int':
#     print(int(el) * 2)
# elif arg == 'real':
#     print(f'{(float(el) * 1.5):.2f}')
# elif arg == 'string':
#     print('$' + el + '$')

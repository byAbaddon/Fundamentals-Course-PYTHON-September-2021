import re

text = input()
digits = ''.join(re.findall(r'\d', text))
alpha = ''.join(re.findall(r'[a-zA-Z]', text))
other = ''.join(re.findall(r'\W', text))

print(f'{digits}\n{alpha}\n{other}')

# --------------------------------------------------(2)--------------------------
# text = input()
# digits, alpha, other = '', '', ''
# for char in text:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         alpha += char
#     else:
#         other += char
#
# print(f'{digits}\n{alpha}\n{other}')


'''
Agd#53Dfg^&4F53
------------------ output:
53453
AgdDfgF
#^&
'''
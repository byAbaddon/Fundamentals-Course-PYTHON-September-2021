products_dict = {}
while True:
    try:
        k, v = input().split(': ')
        if k not in products_dict:
            products_dict[k] = int(v)
        else:
            products_dict[k] += int(v)
    except:
        break

print('Products in stock:')
[print(f'- {k}: {v}') for k, v in products_dict.items()]
print(f'Total Products: {len(products_dict)}\nTotal Quantity: {sum(products_dict.values())}')

# ---------------------------------------------(2)--------------------------
# products_tuple = tuple(x.split(': ') for x in iter(input, 'statistics'))
# products_dict = {}
# for k, v in products_tuple:
#     if products_dict.get(k):
#         products_dict[k] += int(v)
#     else:
#         products_dict[k] = int(v)
#
# print('Products in stock:')
# [print(f'- {k}: {v}') for k, v in products_dict.items()]
# print(f'Total Products: {len(products_dict)}\nTotal Quantity: {sum(products_dict.values())}')





'''
bread: 4
cheese: 2
ham: 1
bread: 1
statistics
'''
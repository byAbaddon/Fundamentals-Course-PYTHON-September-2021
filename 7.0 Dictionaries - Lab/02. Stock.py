stock_list, search_list = [input().split() for _ in range(2)]
stock_dict = dict(zip(stock_list[0::2], stock_list[1::2]))
for product in search_list:
    if stock_dict.get(product):
        print(f'We have {stock_dict[product]} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')


# ---------------------------------------(2)-----------------------
# stock_list = input().split()
# search_products = input().split()
# products = {}
#
# for i in range(0, len(stock_list), 2):
#     products[stock_list[i]] = int(stock_list[i + 1])
#
# for key in search_products:
#     if key in products:
#         print(f'We have {products[key]} of {key} left')
#     else:
#         print(f'Sorry, we don\'t have {key}')


'''
cheese 10 bread 5 ham 10 chocolate 3
jam cheese ham tomatoes
-----------------------
output:
Sorry, we don't have jam
We have 10 of cheese left
We have 10 of ham left
Sorry, we don't have tomatoes
'''

from re import findall

regex_name = r'(?P<name>(?<=%)[A-Z][a-z]+(?=%))'
regex_product = r'<([A-Za-z]+[^\<\>]+)>'
regex_quantity = r'(?<=\|)\d+(?=\|)'
regex_price = r'(\d+\.?\d+(?=\$))'

total_sum = 0

while True:
    text = input()
    if text == 'end of shift':
        break

    name = findall(regex_name, text)
    product = findall(regex_product, text)
    quantity = findall(regex_quantity, text)
    price = findall(regex_price, text)

    if len(name) > 0 and len(product) > 0 and len(quantity) > 0 and len(price) > 0:
        current_sum = float(price[0]) * int(quantity[0])
        print(f'{name[0]}: {product[0]} - {current_sum :.2f}')
        total_sum += current_sum

print(f'Total income: {total_sum:.2f}')


'''
%George%<Croissant>|2|10.3$
%Peter%<Gum>|1|1.3$
%Maria%<Cola>|1|2.4$
end of shift

-------------output:
George: Croissant - 20.60
Peter: Gum - 1.30
Maria: Cola - 2.40
Total income: 24.30
'''
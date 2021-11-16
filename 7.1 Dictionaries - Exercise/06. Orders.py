orders_dict = {}

while True:
    try:
        product, price, quantity = input().split()
        if product not in orders_dict:
            orders_dict[product] = {'price': 0.0, 'quantity': 0}
        orders_dict[product]['price'] = float(price)
        orders_dict[product]['quantity'] += int(quantity)
    except:
        break

for k, v in orders_dict.items():
    print(k, '->', f"{v['quantity'] * v['price']:.2f}")


'''
Beer 2.20 100
IceTea 1.50 50
NukaCola 3.30 80
Water 1.00 500
buy
'''
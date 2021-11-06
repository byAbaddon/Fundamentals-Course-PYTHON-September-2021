product = input()
count = int(input())


def orders(pr, count):
    items = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }
    return f'{(items[pr] * count):.2f}'


print(orders(product, count))

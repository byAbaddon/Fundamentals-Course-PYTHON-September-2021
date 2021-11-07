def add_and_subtract():
    a, b, c = [int(input()) for _ in range(3)]

    def sum_numbers(a1, b1):
        return a1 + b1

    def subtract(num, c1):
        return num - c1

    return subtract(sum_numbers(a, b), c)


print(add_and_subtract())

'''
23
6
10

output: 19
'''
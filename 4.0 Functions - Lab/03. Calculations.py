def calc(*args):
    operator, n1, n2 = [int(x) if x.isdigit() else x for x in args[0]]
    operators = {'multiply': n1 * n2, 'divide': n1 / n2, 'add': n1 + n2, 'subtract': n1 - n2}
    return int(operators[operator])


print(calc([input() for _ in range(3)]))


'''
subtract
5
4

output: 1
'''
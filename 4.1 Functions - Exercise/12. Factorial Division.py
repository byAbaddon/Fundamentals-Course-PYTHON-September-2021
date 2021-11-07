def factorial(n):
    if n != 1:
        return factorial(n - 1) * n
    return n


print(f'{(factorial(int(input())) / factorial(int(input()))):.2f}')


# ------------------------------------------(2)-------------------
# a, b = int(input()), int(input())
#
#
# def recursion(f):
#     if f == 1:
#         return f
#     else:
#         return f * recursion(f - 1)
#
#
# print(f'{(recursion(a) / recursion(b)):.2f}')

'''
5
2

output: 60.00
'''
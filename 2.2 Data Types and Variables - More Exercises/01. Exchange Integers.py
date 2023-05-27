a, b = input(), input()
print(f'Before:\na = {a}\nb = {b}\nAfter:\na = {b}\nb = {a}')

#-----------------------------------------(2)-----------------------
a, b = [int(input()) for _ in range(2)]
print(f'Before:\na = {a}\nb = {b}')
print(f'After:\na = {b}\nb = {a}')

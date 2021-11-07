def odd_even_sum(string):
    odd = sum([int(x) for x in string if int(x) & 1])
    even = sum([int(x) for x in string if not int(x) & 1])
    return f'Odd sum = {odd}, Even sum = {even}'


print(odd_even_sum(input()))

#  1000435
#  output: Odd sum = 9, Even sum = 4

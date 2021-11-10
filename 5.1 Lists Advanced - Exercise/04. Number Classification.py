num_list = list(map(int, input().split(', ')))
print('Positive:', ', '.join([str(x) for x in num_list if x >= 0]))
print('Negative:', ', '.join([str(x) for x in num_list if x < 0]))
print('Even:', ', '.join([str(x) for x in num_list if not x & 1]))
print('Odd:', ', '.join([str(x) for x in num_list if x & 1]))

# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33

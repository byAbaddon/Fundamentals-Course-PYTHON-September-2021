num_list = list(map(int, input().split(' ')))
remove_count = int(input())
copy_list = sorted(num_list.copy())[remove_count:]

print(', '.join([str(n) for n in num_list if n in copy_list]))


'''
1 10 2 9 3 8
2

output: 10, 9, 3, 8
'''
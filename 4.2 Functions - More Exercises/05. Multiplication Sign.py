num_list = [int(input()) for _ in range(3)]
negatives = len([x for x in num_list if x < 0])
print('zero' if num_list.count(0) > 0 else 'negative' if (negatives == 1 or negatives == 3) else 'positive')


'''
2
-3
-1

output: positive
'''

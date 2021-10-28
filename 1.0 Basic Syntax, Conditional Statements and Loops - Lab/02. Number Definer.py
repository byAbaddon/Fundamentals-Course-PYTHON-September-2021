# 02. Number Definer
num = float(input())
result = ''

if num == 0:
    result = 'zero'
elif 0 < num < 1:
    result = 'small positive'
elif 1 <= num < 1000000:
    result = 'positive'
elif num >= 1000000:
    result = 'large positive'
else:
    if abs(num) < 1:
        result = 'small negative'
    elif abs(num) > 1000000:
        result = 'large negative'
    else:
        result = 'negative'

print(result)

'''
25
0.7
435247392.921
-0.005
-103.21
-358583355123.001
'''

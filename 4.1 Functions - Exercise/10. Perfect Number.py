n = int(input())
num_sum = 0
for i in range(1, n):
    if n % i == 0:
        num_sum += i

print('We have a perfect number!' if num_sum == n else 'It\'s not so perfect.')

# 6

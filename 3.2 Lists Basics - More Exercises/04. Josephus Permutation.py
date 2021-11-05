arr = (list(map(int, input().split(' '))))
n = int(input()) - 1

result = ''
index = 0

while arr:
    index = (index + n) % len(arr)
    result += str(arr.pop(index))

print('[' + ','.join(result) + ']')


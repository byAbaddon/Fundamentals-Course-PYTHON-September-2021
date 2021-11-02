snowballs = int(input())
collection = {}
snowball_value = 0

while snowballs:
    snowball_snow, snowball_time, snowball_quality, = [int(input()) for _ in range(3)]

    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    collection[snowball_value] = f'{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})'

    snowballs -= 1

for key, value in sorted(collection.items(), reverse=True):
    print(value)
    break


'''
2
10
2
3
5
5
5

output: 10 : 2 = 125 (3)
'''
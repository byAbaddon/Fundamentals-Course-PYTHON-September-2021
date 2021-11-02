n = int(input())
collection = [int(input()) for _ in range(n)]
liters = 255
total = 0

while collection:
    lt = collection.pop(0)
    if liters >= lt:
        liters -= lt
        total += lt
    else:
        print('Insufficient capacity!')

print(total)

for i in range(1, int(input()) + 1):
    f = i % 10
    s = i / 10
    result = int(f + s)

    if result == 5 or result == 7 or result == 11:
        print(i, '-> True')
    else:
        print(i, '-> False')

# 15

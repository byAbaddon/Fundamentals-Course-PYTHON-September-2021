print(list(map(int, filter(lambda x: not int(x) & 1, input().split()))))


# 1 2 3 4
# output: [2, 4]

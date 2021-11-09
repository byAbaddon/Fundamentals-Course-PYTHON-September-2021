print([i for i, d in enumerate(input().split(', ')) if not int(d) & 1])

# ---------------------------------(2)-------------------------------
# arr = list(enumerate(map(int, input().split(', '))))
# print([k for k, v in [arr[i] for i in range(len(arr))] if not v & 1])


# 3, 2, 1, 5, 8
# output: [1, 4]




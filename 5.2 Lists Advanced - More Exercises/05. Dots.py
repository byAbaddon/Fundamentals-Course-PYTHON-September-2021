# TODO...    WTF Fucking Judge ???

SIZE = int(input())
matrix = [input().split() for _ in range(SIZE)]
for r in range(SIZE):
    for c in range(SIZE):
        if matrix[r][c] == '.':
            matrix[r][c] = 1
        else:
            matrix[r][c] = 0


def is_safe(M, row, col, visited):
    return 0 <= row < SIZE and 0 <= col < SIZE and M[row][col] and not visited[row][col]


def dfs(M, row, col, visited, count):
    rowNbr = [-1, +1, 0, 0]
    colNbr = [0, 0, -1, +1]

    visited[row][col] = True

    for k in range(4):
        if is_safe(M, row + rowNbr[k], col + colNbr[k], visited):
            count[0] += 1
            dfs(M, row + rowNbr[k], col + colNbr[k], visited, count)


def largest_region(M):
    visited = [[0] * SIZE for i in range(SIZE)]
    result = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if M[i][j] and not visited[i][j]:
                count = [1]
                dfs(M, i, j, visited, count)
                result = max(result, count[0])

    return result


print(largest_region(matrix))




'''
5
. . - - -
. . - - -
- - - - -
- - - . .
- - - . .
--------------
4

'''



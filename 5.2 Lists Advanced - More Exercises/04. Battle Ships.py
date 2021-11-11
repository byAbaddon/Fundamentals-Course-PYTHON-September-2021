n = int(input())
matrix = []
ships_destroyed = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

positions = list(input().split())

for position in positions:
    if matrix[int(position[0])][int(position[2])] != 0:
        matrix[int(position[0])][int(position[2])] -= 1
        if matrix[int(position[0])][int(position[2])] == 0:
            ships_destroyed += 1
    else:
        continue
print(ships_destroyed)
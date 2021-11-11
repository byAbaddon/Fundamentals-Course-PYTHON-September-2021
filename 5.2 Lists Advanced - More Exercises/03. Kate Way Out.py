# ------------------------copy paste-------------
n = int(input())

maze = {}
keys = range(n)
values = []

for k in keys:
    values = list(input())
    maze[k] = values

for r in range(n):
    for c in range(len(values)):
        if maze[r][c] == 'k':
            r_position = r
            c_position = c

moves = 0
exit_maze = False

while True:
    if 0 <= r_position - 1 < n and maze[r_position - 1][c_position] == ' ':
        maze[r_position - 1][c_position] = 'k'
        moves += 1
        r_position = r_position - 1
    elif 0 <= c_position + 1 < len(values) and maze[r_position][c_position + 1] == ' ':
        maze[r_position][c_position + 1] = 'k'
        moves += 1
        c_position = c_position + 1
    elif 0 <= r_position + 1 < n and maze[r_position + 1][c_position] == ' ':
        maze[r_position + 1][c_position] = 'k'
        moves += 1
        r_position = r_position + 1
    elif 0 <= c_position - 1 < len(values) and maze[r_position][c_position - 1] == ' ':
        maze[r_position][c_position - 1] = 'k'
        moves += 1
        c_position = c_position - 1
    else:
        break

if r_position == 0 or r_position == n - 1 or c_position == 0 or c_position == len(values) - 1:
    moves += 1
    exit_maze = True

if exit_maze:
    print(f'Kate got out in {moves} moves')
else:
    print('Kate cannot get out')

# -----------------------------------(2)----------------------- TODO  only 60pts
#
# def find_path(row, col, direction):
#     global step
#
#     if (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1) and maze[row][
#         col] == ' ':  # Check if we have found the exit
#         print(f'Kate got out in {len(step) + 1} moves')
#         exit()
#
#     if maze[row][col] == ' ':  # The current cell is free. Mark it as visited
#         step.append(direction)  # Append the direction to the path
#         maze[row][col] = 'v'
#         # Invoke recursion to explore all possible directions
#         find_path(row, col - 1, 'L')  # left
#         find_path(row - 1, col, 'U')  # up
#         find_path(row, col + 1, 'R')  # right
#         find_path(row + 1, col, 'D')  # down
#
#
# direction = ''
# step = []
# maze = []
# row, col = 0, 0
#
# for i in range(int(input())):
#     current_row = []
#     token = input()
#     for j in range(len(token)):
#         if 'k' in token[j]:
#             row = i
#             col = j
#             current_row.append(' ')
#         else:
#             current_row.append(token[j])
#     maze.append(current_row)
#
# find_path(row, col, direction)
#
# print('Kate cannot get out')

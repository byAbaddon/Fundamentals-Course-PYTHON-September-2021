free_chairs = 0
game_on = True

for room in range(1, int(input()) + 1):
    token = input().split()
    chairs, people = len(token[0]), int(token[1])
    if chairs < people:
        print(f'{people - chairs} more chairs needed in room {room}')
        game_on = False
    else:
        free_chairs += chairs - people

if game_on:
    print(f'Game On, {free_chairs} free chairs left')


'''
4
XXXX 4
XX 1
XXXXXX 3
XXX 3

output: Game On, 4 free chairs left
'''

num = input().split(' ')
l_cars = list(map(int, (num[0:len(num) // 2])))
r_cars = list(map(int, reversed((num[len(num) // 2:]))))[:-1]


def calc_time(car):
    time = 0
    for i in range(len(car)):
        if car[i] == 0:
            time *= 0.8
        else:
            time += car[i]
    return time


l_time = calc_time(l_cars)
r_time = calc_time(r_cars)

if l_time < r_time:
    print(f'The winner is left with total time: {l_time:.1f}')
else:
    print(f'The winner is right with total time: {r_time:.1f}')

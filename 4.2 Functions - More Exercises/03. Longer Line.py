# ------------------------------------------------OMG---------------------------------------------
import math


def point_closer_to_center(x_1, y_1, x_2, y_2):
    first_distance = math.sqrt(abs(x_1) ** 2 + abs(y_1) ** 2)
    second_distance = math.sqrt(abs(x_2) ** 2 + abs(y_2) ** 2)

    if first_distance == second_distance:
        return int(x_1), int(y_1), int(x_2), int(y_2)
    else:
        if first_distance > second_distance:
            return int(x_2), int(y_2), int(x_1), int(y_1)
        else:
            return int(x_1), int(y_1), int(x_2), int(y_2)


def longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    first_line_length = math.sqrt(abs(x_1 - x_2) ** 2 + abs(y_1 - y_2) ** 2)
    second_line_length = math.sqrt(abs(x_3 - x_4) ** 2 + abs(y_3 - y_4) ** 2)

    if first_line_length >= second_line_length:
        return point_closer_to_center(x_1, y_1, x_2, y_2)
    else:
        return point_closer_to_center(x_3, y_3, x_4, y_4)


x1, y1, x2, y2, x3, y3, x4, y4 = [float(input()) for _ in range(8)]
result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(result[:2], end='')
print(result[2:], end='')

'''
2
4
-1
2
-5
-5
4
-3

output: (4, -3)(-5, -5)
'''
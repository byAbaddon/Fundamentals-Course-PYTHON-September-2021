users_points_dict = {}
courses_dict = {}

while True:
    tokens = input().split('-')
    if len(tokens) == 1:
        break
    elif len(tokens) == 2:
        name, ban = tokens[0], tokens[1]
        del users_points_dict[name]
    else:
        name, course, pts = tokens[0], tokens[1], int(tokens[2])
        if name not in users_points_dict:
            users_points_dict[name] = 0

        if users_points_dict[name] < pts:
            users_points_dict[name] = pts

        if course not in courses_dict:
            courses_dict[course] = 0
        courses_dict[course] += 1

sort_user_point_dict = dict(sorted(users_points_dict.items(), key=lambda x: (-x[1], x[0])))
sort_courses_dict = dict(sorted(courses_dict.items(), key=lambda x: (-x[1], x[0])))

print('Results:')
for k, v in sort_user_point_dict.items():
    print(k, '|', v)

print('Submissions:')
for k, v in sort_courses_dict.items():
    print(k, '-', v)


'''
Peter-Java-84
George-C#-84
George-C#-70
Katy-C#-94
exam finished

------------------output:

Results:
Katy | 94
George | 84
Peter | 84
Submissions:
C# - 3
Java - 1
'''
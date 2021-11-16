course_pass = {}
students_dict = {}

while True:
    try:
        course, password = input().split(':')
        if course not in course_pass:
            course_pass[course] = password
    except:
        break

while True:
    tokens = input().split('=>')
    if tokens[0] == 'end of submissions':
        break
    elif len(tokens) == 4:
        course, password, name, pts = [int(i) if i.isdigit() else i for i in tokens]

        if course in course_pass and password in course_pass[course]:
            if name not in students_dict:
                students_dict[name] = {course: pts}
            else:
                if course in students_dict[name]:
                    if pts > students_dict[name][course]:
                        students_dict[name][course] = pts
                else:
                    students_dict[name][course] = pts

winner_name = ''
winner_score = 0

for key, val in students_dict.items():
    current_result = 0
    for k, v in val.items():
        current_result += int(v)
    if current_result > winner_score:
        winner_score = current_result
        winner_name = key
        winner_score = current_result

print(f'Best candidate is {winner_name} with total {winner_score} points.')
print('Ranking:')
sort_students_dict = dict(sorted(students_dict.items()))
for key, val in sort_students_dict.items():
    print(key)
    for k, v in sorted(val.items(), key=lambda x: -x[1]):
        print(f'#  {k} -> {v}')

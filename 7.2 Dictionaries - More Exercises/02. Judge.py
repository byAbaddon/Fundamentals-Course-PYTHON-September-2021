judge_dict = {}  # course  => {name : count}
course_count_dict = {}  # course_name : count
individual_list_dict = {}

while True:
    try:
        name, course, pts = input().split(' -> ')

        if course not in judge_dict:
            judge_dict[course] = {name: int(pts)}
            if course not in course_count_dict:
                course_count_dict[course] = 1
            else:
                course_count_dict.update({course: 1})
        else:

            if name not in judge_dict[course]:
                course_count_dict[course] += 1
                judge_dict[course].update({name: int(pts)})
            if name in judge_dict[course]:
                if int(pts) > judge_dict[course][name]:
                    judge_dict[course][name] = int(pts)
    except:
        break

for key, val in course_count_dict.items():
    counter = 0
    print(f'{key}: {val} participants')
    sort_judge_dict = dict(sorted(judge_dict[key].items(), key=lambda x: (-x[1], x[0])))
    for name, pts in sort_judge_dict.items():
        counter += 1
        print(f'{counter}. {name} <::> {pts}')
        if name not in individual_list_dict:
            individual_list_dict[name] = 0
        individual_list_dict[name] += pts

sort_individual_list_dict = dict(sorted(individual_list_dict.items(), key=lambda x: (-x[1], x[0])))
print('Individual standings:')
counter = 1
for k, v in sort_individual_list_dict.items():
    print(f'{counter}. {k} -> {v}')
    counter += 1


'''
Pesho -> Algo -> 400
Gosho -> Algo -> 300
Stamat -> Algo -> 200
Pesho -> DS -> 150
Mimi -> DS -> 600
no more time

------------------- output:

Algo: 3 participants
1. Pesho <::> 400
2. Gosho <::> 300
3. Stamat <::> 200
DS: 2 participants
1. Mimi <::> 600
2. Pesho <::> 150
Individual standings:
1. Mimi -> 600
2. Pesho -> 550
3. Gosho -> 300
4. Stamat -> 200
'''
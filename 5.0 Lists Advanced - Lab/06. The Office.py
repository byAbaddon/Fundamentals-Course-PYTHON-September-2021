employees = list(map(int, input().split()))
factor = int(input())
employees = [a * factor for a in employees]
happy = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

if len(happy) >= len(employees) / 2:
    print(f'Score: {len(happy)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(employees)}. Employees are not happy!')

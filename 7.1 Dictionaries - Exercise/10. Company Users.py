data = {}

while True:
    try:
        uni, num = input().split(' -> ')
        if uni not in data:
            data[uni] = []
        data[uni].append(num)
    except:
        break

sort_company = dict(sorted(data.items()))
for k, v in sort_company.items():
    print(k)
    sort = sorted(set(v), key=v.index)
    for num in sort:
        print('--', num)

'''
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

-------------- output:

HP
-- BB12345
Microsoft
-- CC12345
SoftUni
-- AA12345
-- BB12345
'''
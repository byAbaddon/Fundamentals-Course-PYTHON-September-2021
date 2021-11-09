arr = [1]

for i in range(1, int(input())):
    if i >= 3:
        arr.append(sum(arr[-3:]))
    else:
        arr.append(i)
            
print(*arr)
    

'''
4
output: 1 1 2 4
'''
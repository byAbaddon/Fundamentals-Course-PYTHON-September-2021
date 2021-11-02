key = int(input())
print(''.join([chr(ord(input()) + key) for _ in range(int(input()))]))

'''
3
7
P
l
c
q
R
k
f

output: SoftUni
'''

stack = []
is_balanced = True

for _ in range(int(input())):
    line = input().strip()
    if line == '(':
        if stack and stack[-1] == '(':
            is_balanced = False
            break
        stack.append(line)
    elif line == ')':
        if not stack or stack.pop() != '(':
            is_balanced = False
            break
print('BALANCED' if is_balanced and not stack else 'UNBALANCED')

#--------------------------------------------(2)----------------------------------
n = int(input())
collection = [input() for _ in range(n)]
is_open = False
is_closed = True

while collection:
    current = collection.pop(0)

    if current == '(':
        if not is_open:
            is_open = True
        else:
            is_closed = False

    if current == ')':
        if is_open:
            is_open = False
        else:
            is_closed = False

if is_closed and not is_open:
    print('BALANCED')
else:
    print('UNBALANCED')

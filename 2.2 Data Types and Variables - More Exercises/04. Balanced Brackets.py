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

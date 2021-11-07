def asci():
    start, end = [ord(input()) for i in range(2)]
    return [chr(x) for x in range(start + 1, end)]


print(*asci())

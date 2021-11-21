from re import findall

collection = ''

while True:
    data = input()
    if data == '':
        break
    collection += data

result = findall(r'\d+', collection)
print(' '.join(result))


'''
The300
What is that?
I think it's the 3rd movie 
Lets watch it at 22:45

--------------------output:
300 3 22 45

'''
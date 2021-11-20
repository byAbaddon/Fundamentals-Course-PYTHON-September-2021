f_char, l_char = ord(input()), ord(input())
text = list(map(lambda x: ord(x), input()))
result = sum(filter(lambda x: f_char < x < l_char, text))
print(result)


'''
.
@
dsg12gr5653feee5

-----------------output:
363
'''
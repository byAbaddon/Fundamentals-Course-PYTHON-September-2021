text = input()

for i in range(len(text)):
    try:
        if text[i] != text[i + 1]:
            print(text[i], end='')
    except:
        print(text[i], end='')


'''
aaaaabbbbbcdddeeeedssaa

-------------------output:
abcdedsa'
'''


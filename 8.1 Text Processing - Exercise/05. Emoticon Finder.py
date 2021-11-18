text = input()
[print(text[i] + text[i + 1]) for i in range(len(text)) if text[i] == ':']


'''
There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)

--------------output: 
:P
:O
:)
'''

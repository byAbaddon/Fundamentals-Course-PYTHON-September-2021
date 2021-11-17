ban_words = input().split(', ')
text = input()

for ban in ban_words:
    text = text.replace(ban, '*' * len(ban))

print(text)

'''
Linux, Windows
It is not Linux, it is Windows, Mac!
------------------ output:
It is not *****, it is *******, Mac!
'''
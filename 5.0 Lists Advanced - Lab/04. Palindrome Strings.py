word_list = input().split()
match = input()
word_list = [word for word in word_list if word == word[::-1]]
print(f'{word_list}\nFound palindrome {word_list.count(match)} times')

'''
wow father mom wow shirt stats
wow

output:
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times
'''
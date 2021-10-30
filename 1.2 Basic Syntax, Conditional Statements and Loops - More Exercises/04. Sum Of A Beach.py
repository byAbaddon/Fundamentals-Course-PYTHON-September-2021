import re

word = input().lower()
regex = r"fish|sun|sand|water"
matches = re.findall(regex, word)
print(len(matches))

'''
GolDeNSanDyWateRyBeaChSuNN
output: 3
'''

# --------------------------(2)--------------------------

# word = input().lower()
# count = 0
#
# for i in range(len(word)):
#   if word[i] == 'f':
#     if word[i: i+4] == 'fish':
#       count += 1
#   elif word[i] == 's':
#     if word[i: i+3] == 'sun':
#        count += 1
#     elif word[i: i+4] == 'sand':
#        count += 1
#   elif word[i] == 'w':
#     if word[i: i+5] == 'water':
#        count += 1
#
# print(count)
#
#
#

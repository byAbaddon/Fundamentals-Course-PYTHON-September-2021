import re

collection = []
result = re.findall(r'\b[^\w]_{1}[A-Za-z\d]+\b', input())

for word in result:
    collection.append(word.strip()[1:])

print(','.join(collection))

'''
The _id and _age variables are both integers.

-------------output:
id, age
'''
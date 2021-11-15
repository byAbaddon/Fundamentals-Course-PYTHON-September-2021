synonyms = {}

for _ in range(int(input())):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms:
    print(f'{key} - {", ".join(synonyms[key])}')

'''
2
task
problem
task
assignment
----------

output:
task – problem, assignment
'''
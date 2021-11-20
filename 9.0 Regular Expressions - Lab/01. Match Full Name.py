from re import findall

names_list = input()
regex = r"(\b[A-Z]{1}[a-z]+\s{1}[A-Z]{1}[a-z]+\b)"
result = findall(regex, names_list)
print(*result)


'''
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett

------------------output:
Peter Smith Lily Everett
'''
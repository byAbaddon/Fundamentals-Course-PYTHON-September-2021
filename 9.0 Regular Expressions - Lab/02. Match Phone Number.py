from re import findall

numbers = input()
regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
result = findall(regex, numbers)
print(', '.join(result))


'''
+359 2 222 2222,359-2-222-2222, +359-2-222-22222 +359-2-222-2222

----------output:
+359 2 222 2222, +359-2-222-2222
'''
from re import findall

text = input()
regex = r'((?<=\s)[a-z0-9]+([\.\-_]?[a-z0-9]+)*@[a-z0-9]+([\.\-_]?[a-z0-9]+)*\.[a-z0-9]+([\.\-_]?[a-z0-9]+)*)'
for result in findall(regex, text):
    print(result[0])

'''
Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.

--------------------output:
s.miller@mit.edu
j.hopking@york.ac.uk
'''
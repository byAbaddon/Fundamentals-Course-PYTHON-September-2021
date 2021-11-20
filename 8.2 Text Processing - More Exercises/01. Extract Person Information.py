from re import findall

re_name = r'(?<=@)(.*)(?=\|)'
re_age = r'(?<=#)(.*)(?=\*)'

for _ in range(int(input())):
    text = input()
    find_name = findall(re_name, text)
    find_age = findall(re_age, text)
    print(f'{find_name[0]} is {find_age[0]} years old.')


'''
2
Here is a name @George| and an age #18*
Another name @Billy| #35* is his age

----------------output:
George is 18 years old.
Billy is 35 years old.
'''
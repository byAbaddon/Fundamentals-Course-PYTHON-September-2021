data = input().split()
alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
            'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26}
total_sum = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])

    if first_letter.isupper():
        total_sum += number / alphabet[first_letter]
    else:
        total_sum += number * alphabet[first_letter.upper()]

    if last_letter.isupper():
        total_sum -= alphabet[last_letter]
    else:
        total_sum += alphabet[last_letter.upper()]

print(f'{total_sum:.2f}')


'''
A12b s17G

-------------------output:
330.00
'''
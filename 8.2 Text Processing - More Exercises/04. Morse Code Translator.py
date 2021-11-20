data = input().split(' | ')
result = []

morse_alphabet = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                '--.': 'G', '....': 'H',  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

for word in data:
    current = ''
    for i in word.split():
        current += morse_alphabet[i]
    result.append(current)       

print(*result)

'''
.. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .

--------------output:
I MADE YOU WRITE A LONG CODE
'''
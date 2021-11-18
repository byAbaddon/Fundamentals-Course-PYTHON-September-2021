text = input()
index, explosions = 0, 0

while index < len(text):
    char = text[index]
    if char == '>':
        explosions += int(text[index + 1])
    elif explosions > 0:
        text= text[:index] + text[index + 1:]
        index -= 1
        explosions -= 1 
    index += 1

print(text)


'''
abv>1>1>2>2asdasd

----------------output:
abv>>>>dasd
'''
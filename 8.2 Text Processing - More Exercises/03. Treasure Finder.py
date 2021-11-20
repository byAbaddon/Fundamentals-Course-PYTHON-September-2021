from re import findall

keys = input().split()

while True:
    command = input()
    if command == 'find':
        break
    message, number = '', ''
    index = 0

    for char in command:
        if index == len(keys):
            index = 0
        number = ord(char) - int(keys[index])
        message += chr(number)
        index += 1

    regex = r"(?<=&)(.*)(?=&)|(?<=<)(.*)(?=>)"
    result = findall(regex, message)
    print(f'Found {result[0][0]} at {result[1][1]}')


# ----------------------------------(2)-------- time limit------------------

# keys = input().split()
#
# while True:
#     command = input()
#     if command == 'find':
#         break
#     message, number = '', ''
    # index = 0
    #
    # for char in command:
    #     if index == len(keys):
    #         index = 0
    #     number = ord(char) - int(keys[index])
    #     message += chr(number)
    #     index += 1
    #
    #
    # def get_element(element):
    #     start_index = message.find(element)
    #     if element == '<':
    #         last_index = message.rfind('>')
    #     else:
    #         last_index = message.rfind(element)
    #
    #     result = message[start_index + 1: last_index]
    #     return result
    #
    # print(f"Found {get_element('&')} at {get_element('<')}")



'''
1 2 1 3
ikegfp'jpne)bv=41P83X@
ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
find

--------------------output:
Found gold at 10N70W
Found Silver at 32S43W

'''
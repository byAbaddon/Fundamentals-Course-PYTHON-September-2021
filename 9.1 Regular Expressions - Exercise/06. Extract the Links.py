from re import finditer

pattern = r'\bwww\.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-z]+)+\b'

while True:
    command = input()
    if command == '':
        break

    for email in finditer(pattern, command):
        print(email[0])


'''
Join WebStars now for free, at www.web-stars.com 
You can also support our partners:
Internet - www.internet.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko

-------------------------output:
www.web-stars.com
www.internet.com
www.webspiders101.com
'''
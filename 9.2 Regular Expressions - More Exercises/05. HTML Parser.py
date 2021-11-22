import re

info = input()
title_regex = r'<title>([^<>]*)<\/title>'
title = re.findall(title_regex, info)
title = ''.join(title)

print(f"Title: {title}")

body_regex = r'<body>.*<\/body>'
body = re.findall(body_regex, info)
body = ''.join(body)

content_regex = r">([^><]*)<"
content = re.findall(content_regex, body)
content = ''.join(content)
content = content.replace('\\n', '')
print(f'Content: {content}')


# -------------------------------------------------------(2)-------------80 pts   TODO

# from re import finditer
#
# text = input()
# regex = r"(^|(?<=\>)|(?<=\\n)|(?<=\>))[\w \.\-]+"
# result = finditer(regex, text)
# collection = [x.group() for x in result]
#
# print(f'Title: {collection[0]}')
# print('Content:', *[x.strip() for x in collection[1:]])


'''
<html>\n<head><title>Some title</title></head>\n<body>Here<p>is some</p>content<a href="www.somesite.com">\nclick</body>\n</html>

-------------output:
Title: Some title
Content: Here is some content click

'''

import re

text, word = input(), input()
result = re.findall(rf'\b{word}\b', text, re.IGNORECASE)
print(len(result))

'''
The waterfall was so high, that the child couldn't see its peak.
the
-----------output:
2
'''
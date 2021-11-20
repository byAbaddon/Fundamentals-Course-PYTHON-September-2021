title, article = input(), input()

print(f'<h1>\n\t{title}\n</h1>')
print(f'<article>\n\t{article}\n</article>')

while True:
    comment = input()
    if comment == 'end of comments':
        break
    print(f'<div>\n\t{comment}\n</div>')



'''
SoftUni Article
Some content of the SoftUni article
some comment
more comment
last comment
end of comments

-------------------output:
<h1>
    SoftUni Article
</h1>
<article>
    Some content of the SoftUni article
</article>
<div>
    some comment
</div>
<div>
    more comment
</div>
<div>
    last comment
</div>
'''
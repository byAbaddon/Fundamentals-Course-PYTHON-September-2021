text = input()
last_index = text.rfind('\\')
file_name, extension = text[last_index + 1:].split('.')
print(f'File name: {file_name}\nFile extension: {extension}')


'''
C:\Internal\training-internal\Template.pptx
File name: Template
File extension: pptx

-------------------output:
File name: Template
File extension: pptx
'''
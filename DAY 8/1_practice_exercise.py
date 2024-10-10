import os

if os.path.exists('notes.txt'):
    print('File exists')
    with open('notes.txt','r') as file:
        content = file.read()
        print(content)
else:
    print('File does not exist')
    with open('notes.txt','w') as file:
        content = file.write('Hello')
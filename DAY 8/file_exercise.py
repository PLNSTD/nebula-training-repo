movies = ['Interstellar','Django','Kill Bill']
with open('example.txt','w') as file:
    content = file.write('\n'.join(movies))
with open('example.txt','r') as file:
    content = file.read()
print(content)
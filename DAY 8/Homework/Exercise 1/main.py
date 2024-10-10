# 1. Develop a Python script that reads a file and counts the number of words in it.
my_file = open('example.txt', 'r')

content = my_file.read()
my_file.close()

print(f'Words: {content.split()}\n Length:{len(content.split())}')
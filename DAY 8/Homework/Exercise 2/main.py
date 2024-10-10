# 2. Create a program that lists all the files in a given directory and prints their file sizes.
import os
given_directory = '../Exercise 1'

for file_name in os.listdir(given_directory):
    file_size = os.stat(given_directory+f'/{file_name}').st_size
    print(f'File name: \'{file_name}\' {file_size}bytes')
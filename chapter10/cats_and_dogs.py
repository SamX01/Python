# Python
# Programming Python:10-8
# try-except block about cats and dogs
# Xiang Peng
# 2017-12-2

file_name = 'cats.txt'
with open(file_name,'w') as file:
    names = 'Ashe\nBob\nTian'
    contents = file.write(names)


try:
    with open('cats5.txt') as file_obj:
        contents = file_obj.readlines()
except FileNotFoundError:
    pass
else:
    for line in contents:
        print(line.rstrip())

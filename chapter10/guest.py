# 10-3
def name_input(name_number=3):
    num = 0
    name = []
    while num < name_number:
        input_name = input("Please input your name(type 'z' to cancel): ")
        if input_name != 'z':
            name.append(input_name)
            num += 1
        else:
            print('Input Over early')
            break

    print('Input Over')
    return name

names = name_input()
print(names)

file_name = 'input_names.txt'
with open(file_name,'a') as file:
    for name in names:
        file.write("Name:"+name+'\n')

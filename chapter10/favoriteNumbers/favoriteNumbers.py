# Python
# Programming Python 10-11 10-12
# 查找是否存在文件保存喜欢的数字
# 若无，则创建一个文件用于保存
# 若有，则显示
# Xiang Peng
# 2017-12-3

import json

def printMsg(file_name):
    with open(file_name) as obj:
        numbers = json.load(obj)
        message = "I know your favorite numbers!It's "
        while numbers:
            message += numbers.pop()+' and '
        message = message[:-5]+'.'
        print(message)

def getNumber(file_name):
    with open(file_name,'w') as file:
        numbers = []
        while True:
            Flag = input("Do you have a favorite number? ")
            if ((Flag == 'y')or(Flag == 'Y')):
                number = input("Please input your favorite number:")
                numbers.append(number)
                continue
            elif((Flag == 'n')or(Flag == 'N')):
                print("What a shame!")
                break
            else:
                print("Please write in the right word.")
                continue
        json.dump(numbers,file)

file_name = input("Please input your number resource: ")
try:
    printMsg(file_name)
except FileNotFoundError:
    getNumber(file_name)

# Python
# Programming Python:10-6
# This is a simple adder
# Xiang Peng
# 2017-12-2

def isInt(s_num):
    try:
        t_num = int(s_num)
    except ValueError:
        print('You need to type in a number!\n')
        return False 
    else:
        return True


while True:
    print("This is to compute two sum:")

    num1 = input("Num1: ")
    if isInt(num1):
        num2 = input("Num2: ")
        if isInt(num2):
            print(int(num1)+int(num2))
            break


##file_name = 'alicer.txt'
##
##try:
##    with open(file_name) as obj:
##        contents = obj.read()
##except FileNotFoundError:
##    msg = "Sorry,the file "+file_name+' does not exist.'
##    print(msg)
##    #pass
##
##else:
##    words = contents.split()
##    print(len(words))

##print("ddd")
##
##while True:
##
##    num1 = input("num1:")
##    num2 = input("num2:")
##    
##    try:
##        print(int(num1)/int(num2))
##    except ZeroDivisionError:
##        print("Wrong input!")

##try:
##    int('message')
##except TypeError:
##    print("Wrong Answer!")

## 10-4 test
import json
numbers = [2,3,5,6,11,'r']
file_name ='numbers.json'
with open(file_name,'w') as obj:
    json.dump(numbers,obj)



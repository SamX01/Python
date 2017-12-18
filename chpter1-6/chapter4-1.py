#animals = ['dog','cat','bird']
#for animal in animals:
#    print(animal.title()+"s would be a great pet!")

#print('Any of these animals would make a great pet.')

#for value in range(3,6):
#   print(value)

#for num in range(1,21):
#   print(num)

#for num in range(1,20,2):
#   print(num)

#nums = [num**3 for num in range(1,11)] #列表解析

#nums = [num*3 for num in range(1,11)]
#for num in nums:
#    print(num)


a = list(range(3,28,4))
for num in a:
    print(num)
print(len(a))
print('The first three items in the list are:')
print(a[:3])
print(a[-1:3])
print("Three items from the middle of the list are:")
print(a[4:7])
print("The last three items in the list are:")
print(a[-3:])

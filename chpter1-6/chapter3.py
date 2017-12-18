# python programing 3-4

list=[]
list.append('Sam')
list.append('Jack')
list.append('Rose')
print(list)

print('We should invite '+list[0]+' and '+list[1]+' and '+list[2]+' to have dinner!')
print('What a shame that '+list[0]+' could not come.')

list.pop(0)
list.insert(0,'Lily')

print('So we have to invite '+list[0]+' and '+list[1]+' and '+list[2]+' to have dinner!')

print('Surprise!')
print('I just find another larger table,so I can invite more guests.')

list.insert(0,'Frank')
list.insert(3,'Justin')
list.append('Bennett')

def guest_print(guest_list):
    guest_number = 0
    while guest_number < len(list):
        print('Invite '+list[guest_number]+' to come to the dinner')
        guest_number += 1

guest_print(list)

print("Unfortunately,now we have to invite\ntwo VIP guests since we don't have enough money")

def guest_cut(guest_list):
    while len(guest_list) > 2:
        print("Sorry to tell you that we could not invite you, "+guest_list.pop())

guest_cut(list)

print("Dear "+list[0]+",you are still in our inviting list.")
print("Dear "+list[1]+",you are still in our inviting list.")

del list[1]
del list[0]

print(list)




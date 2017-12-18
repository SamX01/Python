import json
file_name = "log2.json"
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

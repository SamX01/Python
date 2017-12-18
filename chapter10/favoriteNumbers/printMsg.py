import json
file_name = 'log2.json'
with open(file_name) as obj:
    numbers = json.load(obj)
    message = "I know your favorite numbers!It's "
    while numbers:
        message += numbers.pop()+' and '
    message = message[:-5]+'.'
    print(message)

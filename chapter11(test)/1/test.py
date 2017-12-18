from f_test import get_formatted_name

print("Enter 'z' to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'z':
        break
    last = input("\nPlease give me a last name:")
    if last == 'z':
        break
    name = get_formatted_name(first,last)
    print("\tNeatly formatted name: " + name + ".")

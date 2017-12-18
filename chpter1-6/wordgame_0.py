import random
secret=random.randint(1,100)

temp=input("Guess the Number:")
guess=int(temp)
while guess!=secret:
    temp=input("Please restart:")
    guess=int(temp)
    if guess==secret:
        print("Right")
        print("There is no bonus")
    else:
        if guess>secret:
            print("High")
        else:
            print("Low")
print("Game Over!^_^")

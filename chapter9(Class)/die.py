from random import randint

class Die():
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        num = randint(1,self.sides)
        print(num)    

def test():
    die1 = Die(10)
    print('Roll the 10-side die')
    for num in range(1,11):
        die1.roll_die()

    print("___________________")
    print('Roll the 20-side die')
    die2 = Die(20)
    for num in range(1,11):
        die2.roll_die()

test()

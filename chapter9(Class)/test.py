class Dog():
    """A class named dog which has some basic behaviours
        and poperities of real dogs"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+' rolled over.')

my_dog = Dog('Huan',12)

## class Restaurant() and its subclass IceCreamStand()
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name.upper())
        print("The cuisine type of the restaurant is "+self.cuisine_type.upper())

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self,served_guests_number):
        self.number_served = served_guests_number

    def show_number_served(self):
        print(self.number_served)

    def increment_number_served(self,increment):
        if self.number_served:
            self.number_served += increment
        else:
            print('Error!')

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def add_flavors(self,flavor):
        self.flavors.append(flavor)

    def show_flavors(self):
        flavors=self.flavors
        print("So many flavors for the icecream.")
        while flavors:
            print(flavors.pop().title())
        print('Is there one of your favorite flavors?')
    

def test1():
    jianggu = Restaurant('wuji','bbb')
    jianggu.describe_restaurant()
    jianggu.open_restaurant()
##    jianggu.set_number_served(33)
##    jianggu.show_number_served()
##    jianggu.increment_number_served(20)
##    jianggu.show_number_served()
    tianji = IceCreamStand('tianji','ccc')
    tianji.add_flavors('ddd')
    tianji.add_flavors('dfas')
    tianji.show_flavors()
    

tianji = IceCreamStand('tianji','ccc')
tianji.add_flavors('ddd')
tianji.add_flavors('dfas')
tianji.show_flavors()


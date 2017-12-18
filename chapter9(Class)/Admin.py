from User import User


class Admin(User):
    def __init__(self,first_name,last_name,**other_info):
        super().__init__(first_name,last_name,**other_info)
        self.privileges = Privileges()

class Privileges():
   # def __init__(self,privileges=['can add post','can delete post','can ban user']):
    #    self.privileges = privileges
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
        
    def show_privileges(self):
        print('ther are such privileges for the admins:')
        privileges = self.privileges
        while privileges:
            print(privileges.pop().upper())
        print('Over!')

class User():
    def __init__(self,first_name,last_name,**other_info):
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info
        self.login_attempts = 0

    def describe_user(self):
        print("User:")
        print("     First Name:"+self.first_name.title())
        print("     Last Name:"+self.last_name.title())
        if self.other_info:
            print("Additional info:")
            for key,value in self.other_info.items():
                print("     "+key.title()+':'+str(value))
    def greet_user(self):
        print("Greetings!"+self.first_name.title()+' '+self.last_name.title())    

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        print('Reset login attempt number!')
        self.login_attempts = 0
        
    def show_login_attempts(self):
        print("Login Attempt:"+str(self.login_attempts))



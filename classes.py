class User:
    """
    Class that generrates new instances of users
    """
    users_list = []

    def __init__(self,first_name,last_name,phone_number,email,username,password):
        """
        method to define properties for each user object
        """
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)

    def delete_user(self):
        '''
        Function to delete user information
        '''
        User.users_list.remove(self)    

class Credentials:
    """
    Class that generrates new instances of users credentials
    """
    credential_list = []
    user_crediatials_list = []

    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and password entered match entries in the user_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.username == username and user.password == password):
                current_user = user.username
                return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''
        

        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password


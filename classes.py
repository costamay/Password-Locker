class User:
    """
    Class that generrates new instances of users
    """
    user_list = []

    def __init__(self,first_name,last_name,phone_number,email,password):
        """
        method to define properties for each user object
        """
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

class Credentials:
    """
    Class that generrates new instances of users credentials
    """
    credential_list = []
    user_crediatials_list = []

    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''
        

        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password


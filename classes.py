class User:
    """
    Class that generrates new instances of contacts
    """

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




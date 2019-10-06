from classes import User
from classes import Credential
import unittest
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            'titus', 'nad', 'titusouko@gmail.com', '0727719206', '1234')

    def test__init__(self):
        self.assertEqual(self.new_user.first_name, 'titus')
        self.assertEqual(self.new_user.last_name, 'nad')
        self.assertEqual(self.new_user.email, 'titusouko@gmail.com')
        self.assertEqual(self.new_user.phone_number, '0727719206')
        self.assertEqual(self.new_user.password, '1234')

    def tearDown(self):
        Credential.credential_list = []
        User.users_list = []

    def test_save_user(self):
        '''
        Method to test if we can save the user details
        '''

        self.new_user.save_user()
        test_user = User('titus', 'nad', 'titusouko@gmail.com',
                         '0727719206', '1234')
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        '''
        Method to test if we can delete a user
        '''

        self.new_user.save_user()
        test_user = User('titus', 'nad', 'alexnad425@gmail.com',
                         '0727719206', '1234')
        test_user.save_user()

        test_user.delete_user()
        self.assertEqual(len(User.users_list), 1)


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential(
            'titus', 'twitter', '12345')

    def test__init__(self):
        self.assertEqual(self.new_credential.user_name, 'titus')
        self.assertEqual(self.new_credential.site_name, 'twitter')
        self.assertEqual(self.new_credential.password, '12345')

# Testing credentials

    def tearDown(self):
        Credential.credential_list = []
        User.users_list = []

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential('titus', 'twitter', '12345')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential('titus', 'twitter', 'alex-muliande', '12345')
        twitter.save_credentials()
        twitter.delete_credentials()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_account_type method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('alex', 'twitter', 'alex-muliande', '12345')
        twitter.save_credentials()
        credential_found = Credential.find_by_site_name('twitter')
        self.assertEqual(credential_found, twitter)

  

if __name__ == '__main__':
    unittest.main()

  
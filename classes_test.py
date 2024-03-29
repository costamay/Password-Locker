from classes import User
from classes import Credentials
import unittest
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Titus', 'Opiyo', '0705413505','titusouko@gmail.com','costamay', '1234')

    def test__init__(self):
        self.assertEqual(self.new_user.first_name, 'Titus')
        self.assertEqual(self.new_user.last_name, 'Opiyo')
        self.assertEqual(self.new_user.phone_number, '0705413505')
        self.assertEqual(self.new_user.email, 'titusouko@gmail.com')
        self.assertEqual(self.new_user.username, 'costamay')
        self.assertEqual(self.new_user.password, '1234')

    def tearDown(self):
        Credentials.credential_list = []
        User.users_list = []

    def test_save_user(self):
        '''
        Method to test if we can save the user details
        '''

        self.new_user.save_user()
        test_user = User('Titus', 'Opiyo', '0727719206','titusouko@gmail.com','costamay', '1234')
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        '''
        Method to test if we can delete a user
        '''

        self.new_user.save_user()
        test_user = User('Titus', 'Opiyo', '0727719206','titusouko@gmail.com','costamay', '1234')
        test_user.save_user()

        test_user.delete_user()
        self.assertEqual(len(User.users_list), 1)


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials(
            'Titus', 'twitter', '12345')

    def test__init__(self):
        self.assertEqual(self.new_credential.user_name, 'Titus')
        self.assertEqual(self.new_credential.site_name, 'twitter')
        self.assertEqual(self.new_credential.password, '12345')

# Testing credentials

    def tearDown(self):
        Credentials.credential_list = []
        User.users_list = []

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credentials('Titus', 'twitter', '12345')
        twitter.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 2)

    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credentials('Titus', 'twitter', '12345')
        twitter.save_credentials()
        twitter.delete_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_account_type method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credentials('Titus', 'twitter', '12345')
        twitter.save_credentials()
        credential_found = Credentials.find_by_site_name('twitter')
        self.assertEqual(credential_found.site_name, 'twitter')

    def test_copy_credentials(self):
        '''
        A funtcion to test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credentials('Titus', 'twitter', '12345')
        twitter.save_credentials()
        found_credential = None
        for credential in Credentials.credential_list:
            found_credential = Credentials.find_by_site_name(
                credential.site_name)
            return pyperclip.copy(found_credential.password)
        Credentials.copy_credentials(self.new_credential.site_name)
        self.assertEqual('12345', pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main()

  
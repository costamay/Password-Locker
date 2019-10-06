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




if __name__ == '__main__':
    unittest.main()

  
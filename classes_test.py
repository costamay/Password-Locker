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

    
if __name__ == '__main__':
    unittest.main()

  
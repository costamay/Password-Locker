from classes import User
from classes import Credential
import unittest
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            'titus', 'nad', 'titusouko@gmail.com', '0727719206', '1234')

  

if __name__ == '__main__':
    unittest.main()

  
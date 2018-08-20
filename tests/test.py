import unittest
import json
import time
from app.models import User,Questions,Answers





class ApiTestCases(unittest.TestCase):

   def test_user_logged_in(self):
        user = User('username', 'password')
        userSignedUp = user.signup(user)
        self.assertTrue(userSignedUp)
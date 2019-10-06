#!/usr/bin/env python3.6
import pyperclip
from user import User
from user import Credential


def create_user(first_name, last_name, email, phone_number,username, password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name, last_name, phone_number,email, username, password)
    return new_user


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def save_credentials(credential):
    '''
    Function to save a new user account
    '''
    Credential.save_credentials(credential)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(username, password)
    return checking_user


def rand_pass(size):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credential.rand_pass(size)
    # @classmethod
    # def display_credentials(cls,uname):
    #     '''
    #     A class method that displays all credentials of a given username.
    #     '''
    #     return Credentials.display_credentials(cls, uname)


@classmethod
def find_by_site_name(cls, site_name):
    '''
    A function to search for credentials when given an account site search as google, or twitter.
    '''
    return cls.find_by_site_name(cls, site_name)


@classmethod
def copy_credentials(cls, site_name):
    '''
    A class method to enable us to copy credentials of a given site name.
    '''
    return cls.copy_credentials(cls, site_name)



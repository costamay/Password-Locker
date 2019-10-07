#!/usr/bin/env python3.6
import pyperclip
from classes import User
from classes import Credentials


def create_user(first_name, last_name, email, phone_number,username, password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name, last_name, phone_number,email, username, password)
    return new_user


def create_credential(user_name, site_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credentials(user_name, site_name, password)
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
    Credentials.save_credentials(credential)


def verify_user(username, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credentials.check_user(username, password)
    return checking_user


def rand_pass(size):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credentials.rand_pass(size)
   
   
def display_credentials(username):
    '''
    A class method that displays all credentials of a given username.
    '''
    return Credentials.display_credentials(username)


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

def function():
        # print("                            ____         ___   ___                ____      ")
        # print("           |          |   |       |     |     |   |  |\      /|  |          ")
        # print("           |    /\    |   |____   |     |     |   |  | \    / |  |          ")
        # print("           |   /  \   |   |____   |     |     |   |  |  \  /  |  | ___      ")             
        # print("           |  /    \  |   |       |     |     |   |  |   \/   |  |          ")
        # print("           | /      \ |   |       |     |     |   |  |        |  |          ")
        # print("           |/        \|   |____   |____ |____ |___|  |        |  |____      ")              
        # print("                                                                            ")
        print(
        '''

             U _____ u  _        ____   U  ___ u  __  __  U _____ u    
 __        __\| ___"|/ |"|    U /"___|   \/"_ \/U|' \/ '|u\| ___"|/    
 \"\      /"/ |  _|" U | | u  \| | u     | | | |\| |\/| |/ |  _|"      
 /\ \ /\ / /\ | |___  \| |/__  | |/__.-,_| |_| | | |  | |  | |___      
U  \ V  V /  U|_____|  |_____|  \____|\_)-\___/  |_|  |_|  |_____|     
.-,_\ /\ /_,-.<<   >>  //  \\  _// \\      \\   <<,-,,-.   <<   >>     
 \_)-'  '-(_/(__) (__)(_")("_)(__)(__)    (__)   (./  \.) (__) (__)    

        ''')
function()    


def main():
    
    guest_name = input("What is your name?")
    print(f"Hello {guest_name}, welcome to Password Locker:")
    print('\n')
    while True:
        print('\n')
        print(r"*"*30)
        print('\n')
        print("Use these short codes to navigate through Password_Locker:\n ln to log in \n ca to create a new account. \n ex to exit")
        print('\n')

        short_code = input().lower()
        if short_code == 'ca':
            print("New Account")
            print("-"*10)

            print("Enter First Name ... # print("                            ____         ___   ___                ____      ")
        # print("           |          |   |       |     |     |   |  |\      /|  |          ")
        # print("           |    /\    |   |____   |     |     |   |  | \    / |  |          ")
        # print("           |   /  \   |   |____   |     |     |   |  |  \  /  |  | ___      ")             
        # print("           |  /    \  |   |       |     |     |   |  |   \/   |  |          ")
        # print("           | /      \ |   |       |     |     |   |  |        |  |          ")
        # print("           |/        \|   |____   |____ |____ |___|  |        |  |____      ")              
        # print("                                                                            ")")
            first_name = input()

            print("Enter Last Name ...")
            last_name = input()

            print("Enter Phone Number ...")
            phone_number = input()

            print(" Enter Email Address ...")
            email = input()

            print(" Enter Username Address ...")
            username = input()

            

            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
            password_choice = input()
            password = ''

            if password_choice == 'cyo':
                password = password.join(
                    input("Enter a password of your choice..."))
                

            elif password_choice == 'gp':
                print("Enter the length of the password you wish to generate eg 9 ")
                pass_len = int(input())
                password = rand_pass(pass_len)
                

            elif password_choice == 'ex':
                print('Goodbye.........')
                break

            else:
                print("Sorry I didn\'t get that. Please try again")

                
                
            # Create and save new user
            save_user(create_user(first_name, last_name, phone_number,email,username, password))
            print('\n')
            print(f"New Account for {first_name} {last_name} created.")
            print('\n')
            print(
                f"Your password is {password} :-Use it to log in using short code ln")

            print('\n')

        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your username...")
            username = input()
            print("Enter your password...")
            password = input()
            account_exist = verify_user(username, password)
            if account_exist == username:
                print('\n')
                print(
                    f"Welcome to your Password locker account {first_name}: \n Please choose an option to continue...")
                print('\n')
                while True:
                    print('\n')
                    print("Navigation short codes: \n cc to create new credentials: \n dc to display credentials: \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials: \n ex to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter account type... eg \'google\'")
                        site_name = input()
                        print(f"Enter username ")
                        username = input()
                        

                        while True:
                            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit... ")
                            password_choice = input()
                            if password_choice == 'cyo':
                                password = input(
                                    "Enter a password of your choice...")
                                break

                            elif password_choice == 'gp':
                                print(
                                    "Enter the length of the password you wish to generate eg 9 ")
                                pass_len = int(pass_len)
                                password = rand_pass(
                                    pass_len)
                                break

                            elif password_choice == 'ex':
                                print('Goodbye.....')
                                break

                            else:
                                print("Sorry I didn\'t get that. Please try again")

                        

                        save_credentials(create_credential(
                            username, site_name, password))
                        print(' \n')
                        print(
                            f'Credential Created:\n Account type: {site_name}  \n Account Username: {username} \n Account Password: {password}')
                        print('\n ')

                    elif short_code == 'dc':
                        if display_credentials(username):
                            print("Here is a list of your credentials:")
                            print('\n')
                            for credential in display_credentials(username):
                                print(f"Credential Created:\n Account type: {site_name} \n Account Username: {username} \n Account Password: {password}")

                        else:
                            print("You don\'t have any credentials yet")

                    # elif short_code == 'rm':
                    #     print("Enter the account type of the credential you wish to delete:...")
                    #     credential_to_delete = input()
                    #     if find_by_account_type(credential_to_delete):
                    #         credential_to_delete = delete_credentials(credential_to_delete)
                    #         print("Credential successfully deleted!")
                    #     else:
                    #         print(" We couldin\'t find the credentials associated with the account name you typed.")

                    # elif short_code == "copy":
                    #     print(' \n')
                    #     site_name = input(
                    #         'Enter the site name for the credential password to copy: ')
                    #     cls.copy_credentials(site_name)
                    #     print('\n')

                    else:
                        print("I didn\'t get that, please try again")

            else:
                print(
                    f"Sorry, we couldn\'t' find any account under the name {username}")
                print('\n')
        elif short_code == 'ex':
            print('Goodbye...')
            break

        else:
            print("I really did'nt get that, please use the short code ")

print('\n')

if __name__ == '__main__':
    main()
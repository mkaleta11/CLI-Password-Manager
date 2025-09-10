# Password manager class with all methods that create the functionality of the manager
import password_generator
import getpass

class PasswordManager():
    def __init__(self):
        pass

    def view_passwords(self, passwords):
        '''
        Viewing all passwords
        '''
        if not passwords:
            print('No passwords saved yet.')
            return passwords
        
        for key, value in passwords.items():
            print(f'{key}: {value}')
        return passwords
    
    def generate_the_password(self, passwords):
        '''
        Generating a password with possibility of overwriting it
        '''
        user_input = input('What site do you want to generate a password for? ')
        if user_input in passwords:
            user_choice = input(f'A password for {user_input} already exists. Do you want to overwrite it? (y/n): ')
            user_choice = user_choice.lower()
            if user_choice != 'y':
                print('Password not overwritten.')
                return passwords
        passwords[user_input] = password_generator.password_generator()
        return passwords 

    def delete_password(self, passwords):
        '''
        Deleting the password if it exists
        '''
        if not passwords:
            print('No passwords saved yet.')
            return passwords

        print('Here is a list of all sites where you have passwords: ')
        for index, site in enumerate(passwords, 1):
            print(f'{index}: {site}')
        userInput = input('From which site do you want to delete the password: (enter the name) ')

        if userInput in passwords:
            del passwords[userInput]
            return passwords
        else:
            print(f'No password found for {userInput}')
        return passwords
    
    def change_master_password(self):
        print('After you enter your new master password the program will exit' \
        ' and your next login will be done using the new master password.')
        new_master_password = getpass.getpass('(User input hidden for security) Enter new master password: ')
        return new_master_password


# Password manager class with all methods that create the functionality of the manager
import password_generator
import getpass
import os
import tkinter
from tkinter import filedialog

def cyan(text):
    return f'\033[96m{text}\033[0m'

def red(text):
    return f'\033[91m{text}\033[0m'

def green(text):
    return f'\033[92m{text}\033[0m'

class PasswordManager():
    def __init__(self):
        pass

    def view_passwords(self, passwords):
        '''
        Viewing all passwords
        '''
        if not passwords:
            print(red('❌ No passwords saved yet.'))
            return passwords
        
        print(cyan('-------------------------------------------------------------'))
        print(cyan('📋 Here are your passwords: '))
        for key, value in passwords.items():
            print(cyan(f'{key}: \n Username: {value['username']}\n Password: {value['password']}'))
        print(cyan('-------------------------------------------------------------'))
        return passwords
    
    def generate_or_add_password(self, passwords, if_custom_password=False):
        '''
        Generating a password or adding a custom one with possibility of overwritting the password
        '''
        site_name = input(cyan('❔ What site do you want to generate a password for: '))
        if not site_name:
            print(red('❌ The site name cannot be empty.'))
            return passwords
        if site_name in passwords:
            user_choice = input(cyan(f'❔ A password for {site_name} already exists. Do you want to overwrite it? (y/n): '))
            user_choice = user_choice.lower()
            if user_choice != 'y':
                print(red('❌ Password not overwritten.'))
                return passwords
            
        username = input(cyan('❔ What is the username for that site: '))
        if not username:
            print(red('❌ Username cannot be empty.'))
            return passwords
        
        if if_custom_password:
            password = getpass.getpass(cyan('🔒 (User input hidden for security) Enter password: '))
            if not password:
                print(red('❌ Password cannot be empty.'))
                return passwords
            passwords[site_name] = {
                'username': username,
                'password': password,
            }
        else:
            passwords[site_name] = {
                'username': username,
                'password': password_generator.password_generator(),
            }
        print(green('🔑 New password added!'))
        return passwords

    def delete_password(self, passwords):
        '''
        Deleting the password if it exists
        '''
        if not passwords:
            print(red('❌ No passwords saved yet.'))
            return passwords

        print(cyan('📋 Here is a list of all sites where you have passwords: '))
        for index, site in enumerate(passwords, 1):
            print(cyan(f'{index}: {site}'))
        userInput = input(cyan('❔ From which site do you want to delete the password: (enter the name) '))

        if userInput in passwords:
            del passwords[userInput]
            print(green('✅ Password succesfully deleted!'))
            return passwords
        else:
            print(red(f'❌ No password found for {userInput}'))
        return passwords

    
    def change_master_password(self):
        '''
        Changes the master password used for log in
        '''
        print(cyan('After you enter your new master password the program will exit' \
        ' and your next login will be done using the new master password.'))
        while True:
            new_master_password = getpass.getpass(cyan('🔒 (User input hidden for security) Enter new master password: '))
            if not new_master_password:
                print(red('❌ Master password cannot be empty!'))
            else:
                break
        while True:
            enter_again = getpass.getpass(cyan('🔒 (User input hidden for security) Enter new master password again: '))
            if enter_again != new_master_password:
                print(red('❌ Master passwords dont match up. Try again!'))
            else:
                break
        print(green('🗝️  Master password changed succesfully!'))
        return new_master_password
    
    def change_database_path(self):
        '''
        Change the password database path using a folder picker.
        The database file will always be named 'passwords.dat' inside the selected folder.
        '''
        print(cyan('-------------------------------------------------------------'))
        print(cyan('📂 Select a folder where your password database will be stored.'))
        print(cyan('After selection, the program will exit and use this path in the future.'))
        print(cyan('-------------------------------------------------------------'))

        root = tkinter.Tk()
        root.withdraw()

        while True:
            folder_path = filedialog.askdirectory(title="Select folder for password database")

            if not folder_path:
                print(red("❌ No folder selected. Please choose a folder."))
                continue

            if not os.access(folder_path, os.W_OK):
                print(red(f"❌ You do not have write permission in '{folder_path}'."))
                continue

            new_path = os.path.join(folder_path, "passwords.dat")
            break

        with open('password_database_path.txt', 'w') as f:
            f.write(new_path)
        print(green(f"✅ Database path successfully changed to: {new_path}"))
        
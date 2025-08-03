# Simple CLI password manager where you can add a password or delete it.

import password_generator
import json
import os

def generate__delete_password_or_view(passwords):
    '''
    CLI menu where you can choose to genererate or delete the password
    '''
    while True:
        try:
            generate_or_delete_or_view = int(input('Do you want to generate a password, delete it or view all passwords. (type 1/2/3 or 4 to exit the program): '))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if generate_or_delete_or_view == 1:
            generate_the_password(passwords)
        elif generate_or_delete_or_view == 2:
            delete_password(passwords)
        elif generate_or_delete_or_view == 3:
            view_passwords(passwords)
        elif generate_or_delete_or_view == 4:
            break
        else:
            print('Incorrect choice.')
    return passwords

def view_passwords(passwords):
    '''
    Viewing all passwords
    '''
    if not passwords:
        print('No passwords saved yet.')
        return passwords
    
    for key, value in passwords.items():
        print(f'{key}: {value}')
    return passwords

def generate_the_password(passwords):
    '''
    Generating a password with possibility of overwriting it
    '''
    user_input = input('What site do you want to generate a password for? ')
    if user_input in passwords:
        user_choice = input(f'A password for {user_input} already exists. Do you want to overwrite it? (y/n): ')
        user_choice = user_choice.lower()
        if user_choice != 'y':
            print('Exiting the script!')
            return passwords
    passwords[user_input] = password_generator.password_generator()
    return passwords
    
def delete_password(passwords):
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

def save_password_to_computer():
    '''
    Passwords are stored in a JSON file. If it doesn't exist then the JSON file gets created in the same directory.
    '''
    path_file = './passwords.json'

    if os.path.isfile(path_file):
        with open(path_file,'r') as f:
            try:
                passwords = json.load(f)
            except json.JSONDecodeError:
                passwords = {}
    else:
        passwords = {}

    passwords = generate__delete_password_or_view(passwords)


    with open(path_file,'w') as f:
        json.dump(passwords, f, indent=4, sort_keys=True)

        
if __name__ == '__main__':
    save_password_to_computer()
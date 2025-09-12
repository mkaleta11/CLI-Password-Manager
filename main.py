# Simple CLI password manager where you can add, detele or view passwords.
from password_manager_class import PasswordManager
import os
import getpass
import cryptography_functions

with open('password_database_path.txt', 'r') as f:
    PASSWORDS_FILE = f.read().strip()
change_master_password = False
change_database_path = False
password_manager = PasswordManager()

def menu(passwords):
    '''
    CLI menu where you can choose to genererate or delete the password
    '''
    print('-------------------------------------------------------------')
    print('Welcome to LockVault!\nHere is a list of all options in the password manager:' \
    '\n1. Generating a new password' \
    '\n2. Add a custom password' \
    '\n3. Deleting a password' \
    '\n4. Viewing all passwords' \
    '\n5. Exiting the program' \
    '\n6. Changing the master password' \
    '\n7. Changing the path to password database')

    print('-------------------------------------------------------------')
    while True:
        try:
            
            choice = int(input('Enter the number of the action: '))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if choice == 1:
            password_manager.generate_or_add_password(passwords)
        elif choice == 2:
            password_manager.generate_or_add_password(passwords,if_custom_password=True)
        elif choice == 3:
            password_manager.delete_password(passwords)
        elif choice == 4:
            password_manager.view_passwords(passwords)
        elif choice == 5:
            break
        elif choice == 6:
            global change_master_password
            change_master_password = True
            break
        elif choice == 7:
            global change_database_path
            change_database_path = True
            break
        else:
            print('Incorrect choice.')
    return passwords

        
if __name__ == '__main__':
    while True:
        master_password = getpass.getpass('(User input hidden for security) Enter master password: ')
        if not master_password:
            print('Master password cannot be empty!')
        else:
            break

    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE,'rb') as f:
            encrypted_data = f.read()
        try: 
            passwords = cryptography_functions.decrypt_passwords(encrypted_data, master_password)
        except Exception:
            print('Invalid master password!')
            exit(1)
    else:
        passwords = {}

    passwords = menu(passwords)
    if change_master_password:
        master_password = password_manager.change_master_password()
    
    if change_database_path:
        if os.path.exists(PASSWORDS_FILE):
            os.remove(PASSWORDS_FILE)
        password_manager.change_database_path()
        with open('password_database_path.txt', 'r') as f:
            PASSWORDS_FILE = f.read().strip()
        
    with open(PASSWORDS_FILE, 'wb') as f:
        f.write(cryptography_functions.encrypt_passwords(passwords, master_password))

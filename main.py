# Simple CLI password manager where you can add, detele or view passwords.
from password_manager_class import PasswordManager
import os
import getpass
import cryptography_functions
PASSWORDS_FILE = 'passwords.dat'
change_master_password = False
password_manager = PasswordManager()

def menu(passwords):
    '''
    CLI menu where you can choose to genererate or delete the password
    '''
    print('-------------------------------------------------------------')
    print('Welcome to LockVault!\nHere is a list of all options in the password manager:' \
    '\n1. Generating a new password' \
    '\n2. Deleting a password' \
    '\n3. Viewing all passwords' \
    '\n4. Changing the master password' \
    '\n5. Exiting the program')
    print('-------------------------------------------------------------')
    while True:
        try:
            
            choice = int(input('Enter the number of the action: '))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if choice == 1:
            password_manager.generate_the_password(passwords)
        elif choice == 2:
            password_manager.delete_password(passwords)
        elif choice == 3:
            password_manager.view_passwords(passwords)
        elif choice == 4:
            global change_master_password
            change_master_password = True
            break
        elif choice == 5:
            break
        else:
            print('Incorrect choice.')
    return passwords

        
if __name__ == '__main__':
    master_password = getpass.getpass('(User input hidden for security) Enter master password: ')

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
        
    with open(PASSWORDS_FILE, 'wb') as f:
        f.write(cryptography_functions.encrypt_passwords(passwords, master_password))

# Simple CLI password manager where you can add, detele or view passwords.
from password_manager_class import PasswordManager
import os
import getpass
import cryptography_functions
PASSWORDS_FILE = 'passwords.dat'

def menu(passwords):
    '''
    CLI menu where you can choose to genererate or delete the password
    '''
    password_manager = PasswordManager()

    while True:
        try:
            choice = int(input('Do you want to generate a password, delete it or view all passwords. (type 1/2/3 or 4 to exit the program): '))
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
            break
        else:
            print('Incorrect choice.')
    return passwords

        
if __name__ == '__main__':
    master_password = getpass.getpass('Enter master password: ')

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
    with open(PASSWORDS_FILE, 'wb') as f:
        f.write(cryptography_functions.encrypt_passwords(passwords, master_password))

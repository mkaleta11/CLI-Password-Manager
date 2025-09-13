# Simple CLI password manager where you can add, detele or view passwords.
from password_manager_class import PasswordManager
import os
import sys
import time
import getpass
import cryptography_functions

with open('password_database_path.txt', 'r') as f:
    PASSWORDS_FILE = f.read().strip()
change_master_password = False
change_database_path = False
password_manager = PasswordManager()

def print_banner():
    banner = r'''
    ______            _         _   _             _ _   
    |  _  \          (_)       | | | |           | | |  
    | | | |_   _ _ __ _ _ __   | | | | __ _ _   _| | |_ 
    | | | | | | | '__| | '_ \  | | | |/ _` | | | | | __|
    | |/ /| |_| | |  | | | | | \ \_/ / (_| | |_| | | |_ 
    |___/  \__,_|_|  |_|_| |_|  \___/ \__,_|\__,_|_|\__|
    '''
    textBanner = '✨ Your passwords hidden in a Mithril Vault ✨'
    for line in banner.splitlines():
        sys.stdout.write(cyan(f'{line}\n'))
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.02)
    print(cyan(textBanner))
    print()


def cyan(text):
    return f'\033[96m{text}\033[0m'

def red(text):
    return f'\033[91m{text}\033[0m'

def green(text):
    return f'\033[92m{text}\033[0m'

def menu(passwords):
    '''
    CLI menu where you can choose to genererate or delete the password
    '''
    print(cyan('-------------------------------------------------------------'))
    print(cyan('🔐 Welcome to DurinVault!\nHere is a list of all options in the password manager:'))
    print(cyan('-------------------------------------------------------------'))
    print(cyan(
    '1️⃣  Generating a new password' \
    '\n2️⃣  Add a custom password' \
    '\n3️⃣  Deleting a password' \
    '\n4️⃣  Viewing all passwords' \
    '\n5️⃣  Exiting the program' \
    '\n6️⃣  Changing the master password' \
    '\n7️⃣  Changing the path to password database'))

    print(cyan('-------------------------------------------------------------'))
    while True:
        try:
            choice = int(input(cyan('➡️  Enter the number of the action: ')))
        except ValueError:
            print(red('❌ Please enter a valid number.'))
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
            print(cyan('👋 Exiting the program. See you soon!'))
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
            print(red('❌ Incorrect choice.'))
    return passwords

        
if __name__ == '__main__':
    print_banner()
    while True:
        if not os.path.exists(PASSWORDS_FILE):
            print(cyan('Set your master password.'))
            master_password = getpass.getpass(cyan('🔒 (User input hidden for security) Enter master password: '))
            while True:
                enter_again = getpass.getpass(cyan('🔒 (User input hidden for security) Enter master password again: '))
                if enter_again == master_password:
                    break
                else:
                    print(red('❌ Master passwords dont match up. Try again!'))
        else:
            master_password = getpass.getpass(cyan('🔒 (User input hidden for security) Enter master password: '))
        if not master_password:
            print(red('❌ Master password cannot be empty!'))
        else:
            break
    
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE,'rb') as f:
            encrypted_data = f.read()
        try: 
            passwords = cryptography_functions.decrypt_passwords(encrypted_data, master_password)
        except Exception:
            print(red('❌ Invalid master password!'))
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

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
        
        print('-------------------------------------------------------------')
        print('Here are your passwords: ')
        for key, value in passwords.items():
            print(f'{key}: \n Username: {value['username']}\n Password: {value['password']}')
        print('-------------------------------------------------------------')
        return passwords
    
    def generate_or_add_password(self, passwords, if_custom_password=False):
        '''
        Generating a password or adding a custom one with possibility of overwritting the password
        '''
        site_name = input('What site do you want to generate a password for: ')
        if not site_name:
            print('The site name cannot be empty.')
            return passwords
        if site_name in passwords:
            user_choice = input(f'A password for {site_name} already exists. Do you want to overwrite it? (y/n): ')
            user_choice = user_choice.lower()
            if user_choice != 'y':
                print('Password not overwritten.')
                return passwords
            
        username = input('What is the username for that site: ')
        if not username:
            print('Username cannot be empty.')
            return passwords
        
        if if_custom_password:
            password = getpass.getpass('(User input hidden for security) Enter password: ')
            if not password:
                print('Password cannot be empty.')
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
        print('New password added!')
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
            print('Password succesfully deleted!')
            return passwords
        else:
            print(f'No password found for {userInput}')
        return passwords

    
    def change_master_password(self):
        '''
        Changes the master password used for log in
        '''
        print('After you enter your new master password the program will exit' \
        ' and your next login will be done using the new master password.')
        while True:
            new_master_password = getpass.getpass('(User input hidden for security) Enter new master password: ')
            if not new_master_password:
                print('Master password cannot be empty!')
            else:
                break
        print('Master password changed succesfully!')
        return new_master_password
    
    def change_database_path(self):
        '''
        Changing the password database path
        '''
        print('-------------------------------------------------------------')
        print('After you enter the new path the program will exit and the path will be changed for future use.')
        print('Here is an example path that you could write in Windows: C:\\Documents\\Folder\\passwords.dat')
        print('Here is an example path for Linux: /home/username/documents/passwords.dat')
        print('Note that your at the end you should include passwords.dat')
        print('It is advised that you enter a absolute path since there can be some issues if you do otherwise')
        print('-------------------------------------------------------------')
        new_path = input('Enter new path for password database: ')
        if not new_path:
            print('New path cannot be empty.')
        if not new_path.endswith('.dat'):
            print('You have to include passwords.dat at the end.')
        with open('password_database_path.txt', 'w') as f:
            f.write(new_path)
        print(f'Database path changed to: {new_path}')

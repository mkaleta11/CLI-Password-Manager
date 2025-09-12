# CLI-Password-Manager
A CLI password manager that lets you:
- add automatically generated strong passwords
- add your custom password
- delete password 
- view all passwords
- change the master password
- change the file path on which the password database file is saved on
. 
Strong passwords are generated automatically using my own effective algorithm. 
All data is stored in an AES-GCM encrypted file. 
Access is protected by a master password secured with Argon2id.

# Features
- Generate strong passwords
- Add, delete, and view saved passwords
- Change master password
- Change file path
- Encrypted storage with AES-GCM
- Master password protected with Argon2

# How to run
py main.py or python3 main.py

# Requirements
pip install -r requirements.txt

# IMPORTANT
The first time you run the program the master password you provide will be your master password for future use. 
The data is encrypted using this exact master password. 
You must remember the master password because without it you cannot access your password database.
If you forget the master password you will lose access to that database.
You can change the master password but only after logging into the database.
THIS IS FOR SECURITY REASONS TO MAKE THE MANAGER AS SECURE AS POSSIBLE.

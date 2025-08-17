# CLI-Password-Manager
A simple CLI password manager that lets you add, delete, and view passwords. 
Strong passwords are generated automatically and all data is stored in an AES-GCM encrypted file. 
Access is protected by a master password secured with Argon2id.

# Features
- Generate strong passwords
- Add, delete, and view saved passwords
- Encrypted storage with AES-GCM
- Master password protected with Argon2

# How to run
py main.py

# Requirements
pip install cryptography

# IMPORTANT
The first time you run the program the master password you provide will be your master password for future use. 
The data is encrypted using this exact master password. 
You must remember the master password because without it you cannot access your passwords.
If you forget the master password you will lose all your passwords.
The master password cannot be changed.
THIS IS FOR SECURITY REASONS TO MAKE THE MANAGER AS SECURE AS POSSIBLE.

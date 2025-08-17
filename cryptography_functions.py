## All Cryptography functions used in protecting the password files
import os
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

def derive_key(maser_password: str, salt: bytes) -> bytes:
    '''
    Deriving the key using Argon2id, with salt and master_password
    '''
    kdf = Argon2id(salt=salt, length=32, iterations=3, lanes=4, memory_cost=64 * 1024)
    key = kdf.derive(maser_password.encode())
    return key

def encrypt_passwords(passwords: dict, master_password: str) -> bytes:
    '''
    Encrypting passwords with AES GCM algorithm with unique nonce 
    '''
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    data_to_encrypy = json.dumps(passwords).encode()
    encrypted_data = aesgcm.encrypt(nonce, data_to_encrypy, None)
    return salt + nonce + encrypted_data

def decrypt_passwords(data: bytes, master_password: str) -> dict:
    '''
    Decrypting passwords file  
    '''
    salt, nonce, encrypted_data  = data[:16], data[16:28], data[28:]
    key = derive_key(master_password, salt)
    aesgcm = AESGCM(key)
    decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)
    return json.loads(decrypted_data.decode())

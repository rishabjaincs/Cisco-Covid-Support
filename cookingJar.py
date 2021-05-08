from cryptography.fernet import Fernet

def generate_key(keyname):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(keyname, "wb") as key_file:
        key_file.write(key)

def load_key(keyname):
    """
    Load the previously generated key
    """
    return open(keyname, "rb").read()

def encrypt_message(message,keyname):
    """
    Encrypts a message
    """
    key = load_key(keyname)
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print("Please keep the below key handy for further use: ")
    print(encrypted_message)

if __name__ == "__main__":
    keyname=input("Enter the Key Name: ")
    username=input("Enter the Username: ")
    password=input("Enter the Password: ")
    generate_key(keyname)
    encrypt_message("{}:{}".format(username,password),keyname)
from cryptography.fernet import Fernet

# you don't have to use this many times
# the key is well kept
def generate_key():
    """
    Generates a new encryption key.
    """
    return Fernet.generate_key()

def encrypt_file(key, input_file, output_file):
    """
    Encrypts a file using the provided key.
    """
    with open(input_file, 'rb') as file:
        data = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    """
    Decrypts a file using the provided key.
    """
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
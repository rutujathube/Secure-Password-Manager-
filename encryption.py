from cryptography.fernet import Fernet


key = Fernet.generate_key()


cipher = Fernet(key)



def encrypt(password):

    encrypted = cipher.encrypt(
        password.encode()
    )

    return encrypted



def decrypt(password):

    decrypted = cipher.decrypt(
        password
    )

    return decrypted.decode()
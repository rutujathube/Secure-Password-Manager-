import random
import string


def generate():

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(12):
        password += random.choice(chars)

    return password
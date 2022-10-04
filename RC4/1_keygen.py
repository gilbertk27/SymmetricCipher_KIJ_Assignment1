# 0) pip install cryptography
 #   pip install pycryptodome

# 1) Generate a symmetric key
from cryptography.fernet import Fernet
key = Fernet.generate_key()

# 2) Save the key into a file
with open('myTopSecretKey.key', 'wb') as file:
    file.write(key)
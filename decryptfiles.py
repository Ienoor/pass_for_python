import json
import os
from getpass import getpass

from config import gpg


# ToDo finish decrypting files
def decrypt(path: str = os.getenv("PATH_PASSWORD_STORE")) -> dict:
    password = getpass("Введите пароль: ")
    encrypt_files = os.listdir(path)
    data = {}
    for file in encrypt_files:
        file_name = '.'.join(file.split('.')[0:-1])
        data.update(json.loads(str(gpg.decrypt_file(f"store/{file_name}.gpg", passphrase=password))))
    # print(data)
    return data


if __name__ == '__main__':
    decrypt()

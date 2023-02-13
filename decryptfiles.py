import json
import os

import gnupg

gpg = gnupg.GPG(gnupghome="C:/Users/vinog/AppData/Roaming/gnupg")


# ToDo finish decrypting files
def decrypt(path: str) -> dict:
    encrypt_files = os.listdir(path)
    for file in encrypt_files:
        ...
    print(encrypt_files)
    # data = gpg.decrypt_file(path, passphrase=os.getenv('password'))
    # return json.loads(str(data))


if __name__ == '__main__':
    decrypt('./store')

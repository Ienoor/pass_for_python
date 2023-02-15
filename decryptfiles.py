import json
import os
from config import gpg


# ToDo finish decrypting files
def decrypt(path: str) -> dict:
    encrypt_files = os.listdir(path)
    data = {}
    for file in encrypt_files:
        file_name = '.'.join(file.split('.')[0:-1])
        data.update(json.loads(str(gpg.decrypt_file(f"store/{file_name}.gpg", passphrase=os.getenv("PASSWORD")))))

    return data


print(decrypt('./store'))

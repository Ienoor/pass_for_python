import json
import os

import gnupg

gpg = gnupg.GPG(gnupghome="C:/Users/vinog/AppData/Roaming/gnupg")


def reader_gpg(path: str) -> dict:
    data = gpg.decrypt_file(path, passphrase=os.getenv('password'))
    return json.loads(str(data))

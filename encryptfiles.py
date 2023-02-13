import json
import os

import gnupg
from dotenv import load_dotenv

gpg = gnupg.GPG(gnupghome="C:/Users/vinog/AppData/Roaming/gnupg")

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def write_gpg(data: dict):
    with open("tmp.json", 'w') as f:
        json.dump(data, f)
    gpg.encrypt_file(f, recipients=["vinartgen88@yandex.ru"], output='pass.gpg')
    os.remove("tmp.json")

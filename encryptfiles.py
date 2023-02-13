import json
import os

import gnupg
from dotenv import load_dotenv

gpg = gnupg.GPG(gnupghome="C:/Users/vinog/AppData/Roaming/gnupg")

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def encrypt(name: str, login: str, password: str, url: str):
    with open(f"{name}.json", 'w') as f:
        json.dump({
            f"{name}": {
                f"{login}": login,
                f"{password}": password,
                "url": url
            }
        }, f)
    gpg.encrypt_file(f, recipients=[os.getenv('recipients')], output=f"./store/{name}.gpg")
    # os.remove("tmp.json")


if __name__ == '__main__':
    encrypt("ya.com", "tv@kmk.ru", "password", "https://mail.ya.com/")

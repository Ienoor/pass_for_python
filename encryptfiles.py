import json
import os
from config import gpg


def encrypt(name: str, login: str, password: str, url: str):
    with open(f"{name}.json", 'w') as f:
        json.dump({
            f"{name}": {
                f"{login}": login,
                f"{password}": password,
                "url": url
            }
        }, f)
    gpg.encrypt_file(f"{name}.json", recipients=os.getenv("RECIPIENT"), output=f"./store/{name}.gpg")
    os.remove(f"{name}.json")


if __name__ == '__main__':
    encrypt("sad.com", "tv@kmk.ru", "password", "https://vk.com/")

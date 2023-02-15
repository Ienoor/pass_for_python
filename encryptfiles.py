import json
import os

from config import gpg


def encrypt():
    name = input('Введите название: ')
    account = input('Введите аккаунт: ')
    password = input('Введите пароль: ')
    url = input('Url: ')
    if not os.path.isdir("store"):
        os.mkdir('store')
    with open(f"{name}.json", 'w') as f:
        json.dump({
            f"{name}": {
                "account": account,
                "password": password,
                "url": url
            }
        }, f)
    gpg.encrypt_file(f"{name}.json", recipients=os.getenv("RECIPIENT"), output=f"./store/{name}.gpg")
    os.remove(f"{name}.json")


if __name__ == '__main__':
    encrypt()

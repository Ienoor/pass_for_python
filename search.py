import os

import decryptfiles


def search():
    password = decryptfiles.decrypt(os.getenv("PATH_PASSWORD_STORE"))
    name = input('Имя искомого пароля: ')
    return password[name]


if __name__ == '__main__':
    search()

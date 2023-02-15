import os

import decryptfiles


def search():
    data = decryptfiles.decrypt(os.getenv("PATH_PASSWORD_STORE"))
    name = input('Имя искомого пароля: ')
    return data[name]


if __name__ == '__main__':
    search()

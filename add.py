def add_pass():
    name = input('Введите название: ')
    account = input('Введите аккаунт: ')
    password = input('Введите пароль: ')
    add_data = {
        f"{name}": {
            "account": account,
            "password": password
        }
    }
    return add_data

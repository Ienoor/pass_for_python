import os.path


def check_file():
    if not os.path.isfile('./pass.gpg'):
        with open('pass.gpg', 'w') as file:
            file.write('')

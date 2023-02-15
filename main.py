import os

import qargs

import decryptfiles
from password_output import draw
import search
from encryptfiles import encrypt


def main():
    spec = [
        ['add', 'add'],
        ['search', 'search'],
        ['show', 'show'],
    ]

    args = qargs.parse_args(spec)

    if args.add:
        encrypt()
    elif args.search:
        search.search()
    elif args.show:

        print(decryptfiles.decrypt(os.getenv("PATH_PASSWORD_STORE")))


if __name__ == '__main__':
    main()

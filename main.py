import qargs

import search
from display import displaying_all_passwords, password_display
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
        password_display()
    elif args.show:
        displaying_all_passwords()


if __name__ == '__main__':
    main()

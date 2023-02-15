from rich.console import Console
from rich.table import Table
from rich import box

import decryptfiles

console = Console()


def draw(func):
    def wrapper():
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Name", style="dim")
        table.add_column("Login")
        table.add_column("Password", justify="left")
        table.add_column("URL", justify="center")
        data = func()
        for item in data:
            table.add_row(item, data[item]['account'], data[item]['password'], data[item]['url'])

        console.print(table)

    return wrapper


if __name__ == '__main__':
    draw(decryptfiles.decrypt())

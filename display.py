from rich import box
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from decryptfiles import decrypt
from search import search

console = Console()


def displaying_all_passwords():
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Name", style="dim")
    table.add_column("Login")
    table.add_column("Password", justify="left")
    table.add_column("URL", justify="center")
    data = decrypt()
    for item in data:
        table.add_row(item, data[item]['account'], data[item]['password'], data[item]['url'])

    console.print(table)


def password_display():
    data = search()
    login, password, url = data.values()
    print(Panel(
        f"{login}, {password}, {url}", title=f"Найденный пароль", title_align="left", subtitle_align="center"))


if __name__ == '__main__':
    password_display()

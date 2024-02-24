import click
from colorama import Fore
from search import search
"""
TODO: Implement flag -i 
"""

@click.command()
@click.argument("path", required=True)
@click.option("-c", is_flag=True, help="Count of lines that match the pattern")
@click.option("-h", is_flag=True, help="Gives line count and lines no file names")
@click.option("-l", is_flag=True, help="Gives Lonly file names")
@click.option("-n", is_flag=True, help="Gives Line Count and Lines with file names")
@click.option("-v", is_flag=True, help="Inverses the result")
@click.option("-w", is_flag=True, help="Matches lines with whole words")
#@click.option("-i", is_flag=True)
@click.argument("pattern", required=True)
def grep(path: str, c, h, l, n, v, w, pattern: str) -> None:
    #pattern = pattern.lower() if i else pattern
    pattern = rf"(?<!\w){pattern}(?!\w)" if w else pattern
    data: tuple[list[str], list[str], list[str]] = search(path=path, pattern=pattern, inverse=True if v else False)
    if c:
        click.echo(len(data[1]))
    elif h:
        for i in data[1]:
            click.echo(i)
    elif l:
        for i in data[2]:
            click.echo(i)
    elif n:
        for i in data[0]:
            if not i.startswith(path):
                click.echo(i)
            else:
                click.echo(Fore.BLUE + i + Fore.RESET)
    else:
        for i in data[0]:
            if not i.startswith(path):
                click.echo(i[i.index(":") + 2 :])
            else:
                click.echo(Fore.BLUE + i + Fore.RESET)


if __name__ == "__main__":
    grep()

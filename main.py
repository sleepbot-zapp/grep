import click
from colorama import Fore
from search import search
"""
TODO: Implement flag -i 
"""

@click.command()
@click.argument("path", required=True)
@click.option("-c", is_flag=True)
@click.option("-h", is_flag=True)
@click.option("-l", is_flag=True)
@click.option("-n", is_flag=True)
@click.option("-v", is_flag=True)
@click.option("-w", is_flag=True)
#@click.option("-i", is_flag=True)
@click.argument("pattern", required=True)
def grep(path, c, h, l, n, v, w, pattern, i=False, ):

    #pattern = pattern.lower() if i else pattern
    pattern = rf"(?<!\w){pattern}(?!\w)" if w else pattern
    data = search(path=path, pattern=pattern, inverse=True if v else False)
    if c:
        click.echo(len(data[0]))
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

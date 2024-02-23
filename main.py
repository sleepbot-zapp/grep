import click
from colorama import Fore
from search import search

                    
@click.command()
@click.argument('path', required=True)
@click.option("-c", is_flag=True)
@click.option("-h", is_flag=True)
@click.option("-l", is_flag=True)
@click.option("-n", is_flag=True)
@click.option("-v", is_flag=True)
@click.argument('pattern', required=True)
def grep(path, c, h, l, n, v, pattern):
    data = search(path=path, pattern=pattern)
    if v: pass 
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
                click.echo(Fore.BLUE+i+Fore.RESET)
    else:
        for i in data[0]:
            if not i.startswith(path):
                click.echo(i[i.index(":")+1:])
            else:
                click.echo(Fore.BLUE+i+Fore.RESET)

if __name__ == '__main__':
    grep()
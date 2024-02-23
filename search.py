import os
from colorama import Fore
from search_in_file import search_in_file

def search(path, pattern: str):
    """


    Args:
        path (str): takes a file or directory path
        pattern (str): takes a regex string as argument

    Returns:
        tupple[list[str], list[str], list[str]]: 
        x -> line numbers and lines and files
        y -> only lines and line numbers
        z -> only files
    """
    x = []
    y = []
    z = []
    if os.path.isfile(path):
            try:
                lines_with_matches = search_in_file(file=rf"{path}", needle=pattern)
            except Exception:
                ...
            else:
                if lines_with_matches:
                    x.append(f'{path}')
                    z.append(f'{path}')
                else:
                    ...
                for k, l in lines_with_matches.items():
                    for m in l:
                        x.append(f'{k}: {m}')
                        y.append(f'{k}: {m}')
    else:                        
            for i in os.walk(path):
                for j in i[2]:
                    try:
                        lines_with_matches = search_in_file(file=rf"{i[0]}/{j}", needle=pattern)
                    except:
                        continue
                    else:
                        if lines_with_matches:
                            x.append(f'{i[0]}/{j}')
                            z.append(f'{i[0]}/{j}')
                        for k, l in lines_with_matches.items():
                            for m in l:
                                x.append(f'{k}: {m}')  
                                y.append(f'{k}: {m}')    
    return x, y, z
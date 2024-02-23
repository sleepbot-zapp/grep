import os
from search_in_file import search_in_file

def innersearch_file(path, pattern, index):
    x = []
    y = []
    z = []
    try:
        lines_with_matches = search_in_file(file=rf"{path}", needle=pattern)[index]
    except:
        quit()
    else:
        if lines_with_matches:
            x.append(path)
            z.append(path)
        for k, l in lines_with_matches.items():
            for m in l:
                x.append(f'Line {k}: {m}')
                y.append(f'Line {k}: {m}')
    return x, y, z

def innersearch_folder(path, pattern, index):
    x = []
    y = []
    z = []
    for i in os.walk(path):
        for j in i[2]:
            try:
                lines_with_matches = search_in_file(file=rf"{i[0]}/{j}", needle=pattern)[index]
            except:
                         continue
            finally:
                if lines_with_matches:
                    x.append(f'{i[0]}/{j}')
                    z.append(f'{i[0]}/{j}')
                for k, l in lines_with_matches.items():
                    x.append(f'Line {k}: {l}')
                    y.append(f'Line {k}: {l}')    
                for k, l in lines_with_matches.items():
                    for m in l:
                        x.append(f'Line {k}: {m}')  
                        y.append(f'Line {k}: {m}')
    return x, y, z    

def search(path, pattern: str, inverse=False):
    """


    Args:
        path (str): takes a file or directory path
        pattern (str): takes a regex string as argument
        inverse (bool): takes a boolean which inverts the result

    Returns:
        tupple[list[str], list[str], list[str]]: 
        x -> line numbers and lines and files
        y -> only lines and line numbers
        z -> only files
    """
    if not inverse:
        if os.path.isfile(path):
            x, y, z = innersearch_file(path=path, pattern=pattern, index=0)
        else:
            x, y, z = innersearch_folder(path=path, pattern=pattern, index=0)                           
    else:
        if os.path.isfile(path):
            x, y, z = innersearch_file(path=path, pattern=pattern, index=1)
        else:
            x, y, z = innersearch_folder(path=path, pattern=pattern, index=1)                             
    return x, y, z
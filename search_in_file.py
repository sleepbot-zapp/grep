import re
from colorama import Fore as F, Back as B

def search_in_file(file, needle: str):
    """
    Searches for required match type in a specified file

    Args:
        file (file): takes file as argument
        needle (str): takes a regex string as argument

    Returns:
        dict[int, list[str]]: returns a dictionary with matched lines for each line
    """
    with open(file) as f:
        line_number = 0
        lines_with_matches: dict[int, list[str]] = dict()
        for i in f.readlines():
                line_number += 1
                x = re.finditer(rf"{needle}", i)
                for j in x:
                    try:
                        lines_with_matches[line_number].append(f"{F.GREEN}{i[:j.span()[0]]}{F.RESET+B.RED}{i[j.span()[0]:j.span()[1]]}{F.GREEN+B.RESET}{i[j.span()[1]:]}{F.RESET}")
                    except KeyError:
                        lines_with_matches[line_number] = [f"{F.GREEN}{i[:j.span()[0]]}{F.RESET+B.RED}{i[j.span()[0]:j.span()[1]]}{F.GREEN+B.RESET}{i[j.span()[1]:]}{F.RESET}"]
        #print(lines_with_matches)
        # print(lines_without_matches)
        return lines_with_matches
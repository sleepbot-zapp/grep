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
        line_number = 1
        lines_with_matches: dict[int, list[str]] = dict()
        lines_without_matches: dict[int, list[str]] = dict()
        lines = f.readlines()
        for i in lines:
            i = i.replace("\n", "") if needle != r"\n" else i
            x = re.finditer(rf"{needle}", i)
            s = list(x)
            if s:
                for j in s:
                    try:
                        lines_with_matches[line_number].append(
                            F.GREEN
                            + i[: j.span()[0]]
                            + F.RESET
                            + B.RED
                            + i[j.span()[0] : j.span()[1]]
                            + F.GREEN
                            + B.RESET
                            + i[j.span()[1] :]
                            + F.RESET
                        )
                    except KeyError:
                        lines_with_matches[line_number] = [
                            F.GREEN
                            + i[: j.span()[0]]
                            + F.RESET
                            + B.RED
                            + i[j.span()[0] : j.span()[1]]
                            + F.GREEN
                            + B.RESET
                            + i[j.span()[1] :]
                            + F.RESET
                        ]
            else:
                lines_without_matches[line_number] = [F.RED + i + F.RESET]
            line_number += 1
        return lines_with_matches, lines_without_matches

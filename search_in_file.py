import re
from colorama import Fore as F, Back as B
from io import TextIOWrapper


def search_in_file(file: TextIOWrapper, needle: str) -> tuple[dict[int, list[str]], dict[int, list[str]]]:
    """
    Searches for required match type in a specified file

    Args:
        file (file): takes file as argument
        needle (str): takes a regex string as argument
        is_casinsesitive (bool): toggles case sensitivity

    Returns:
        dict[int, list[str]]: returns a dictionary with matched lines for each line
    """
    with open(file) as f:
        line_number: int = 1
        lines_with_matches: dict[int, list[str]] = dict()
        lines_without_matches: dict[int, list[str]] = dict()
        lines: list[str] = f.readlines()
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

#!/usr/bin/env python3
"""Task 9"""


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    """
    Calculate the length of each element in the list
    """
    return [(i, len(i)) for i in lst]

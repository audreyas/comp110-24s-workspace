"""Functions that either mutate a list or don't."""

def remove_first(input_list: list[str]) -> None: 
    """remove first element of input_list. Mutating!"""
    input_list.pop(0)

def get_first(input_list: list[str]) -> str:
    """Return first elemnet of input_list without mutating."""
    return input_list[0]

def get_and_remove_first(input_list: list[str]) -> str:
    """Return first eleemnt AND remove it."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem
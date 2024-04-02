"""Mutating functions."""

__author__ = "730387535"


def manual_append(a: list[int], b: int) -> None: 
    """Mutates input appending b to the end of a."""
    a.append(b)
    

def double(a: list[int]) -> None: 
    """Mutates input by multiplying every eleemnt in a by 2."""
    index = 0 
    while index < len(a): 
        a[index] *= 2
        index += 1